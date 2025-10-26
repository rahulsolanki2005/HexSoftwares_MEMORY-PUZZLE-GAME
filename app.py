import tkinter as tk
from tkinter import messagebox, font
import random
import time

class MemoryPuzzleGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Puzzle Game")
        self.root.geometry("900x850")
        self.root.configure(bg="#1a1a2e")
        self.root.resizable(True, True)
        
        # Game variables
        self.difficulty = None
        self.cards = []
        self.card_buttons = []
        self.first_card = None
        self.second_card = None
        self.matches_found = 0
        self.moves = 0
        self.time_limit = 0
        self.start_time = None
        self.timer_running = False
        self.can_click = True
        self.high_scores = {"Easy": float('inf'), "Medium": float('inf'), "Hard": float('inf')}
        
        # Emojis for cards (16 different pairs)
        self.emojis = ['🎮', '🎯', '🎲', '🎪', '🎨', '🎭', '🎬', '🎤', 
                       '🎧', '🎸', '🎹', '🎺', '🎻', '🏀', '⚽', '🏈']
        
        self.show_main_menu()
    
    def show_main_menu(self):
        self.clear_window()
        
        # Main container with scrollbar support
        main_container = tk.Frame(self.root, bg="#1a1a2e")
        main_container.pack(fill=tk.BOTH, expand=True)
        
        # Title
        title_font = font.Font(family="Arial", size=32, weight="bold")
        title = tk.Label(main_container, text="Memory Puzzle", font=title_font, 
                        bg="#1a1a2e", fg="#00d4ff")
        title.pack(pady=30)
        
        subtitle = tk.Label(main_container, text="Match all the pairs before time runs out!", 
                           font=("Arial", 13), bg="#1a1a2e", fg="#ffffff")
        subtitle.pack(pady=5)
        
        # Difficulty buttons
        button_frame = tk.Frame(main_container, bg="#1a1a2e")
        button_frame.pack(pady=30)
        
        difficulties = [
            ("Easy", "4x4 Grid • 90 seconds", "#4CAF50", 90),
            ("Medium", "4x4 Grid • 60 seconds", "#FF9800", 60),
            ("Hard", "4x4 Grid • 45 seconds", "#F44336", 45)
        ]
        
        for diff, desc, color, time_limit in difficulties:
            btn_frame = tk.Frame(button_frame, bg="#1a1a2e")
            btn_frame.pack(pady=12)
            
            btn = tk.Button(btn_frame, text=diff, font=("Arial", 16, "bold"),
                          bg=color, fg="white", width=15, height=2,
                          command=lambda d=diff, t=time_limit: self.start_game(d, t),
                          cursor="hand2", relief=tk.RAISED, bd=3)
            btn.pack()
            
            desc_label = tk.Label(btn_frame, text=desc, font=("Arial", 10),
                                bg="#1a1a2e", fg="#aaaaaa")
            desc_label.pack()
        
        # High scores
        scores_frame = tk.Frame(main_container, bg="#1a1a2e")
        scores_frame.pack(pady=25)
        
        tk.Label(scores_frame, text="🏆 Best Times 🏆", font=("Arial", 15, "bold"),
                bg="#1a1a2e", fg="#ffd700").pack()
        
        for diff in ["Easy", "Medium", "Hard"]:
            score_text = f"{diff}: {self.high_scores[diff]} moves" if self.high_scores[diff] != float('inf') else f"{diff}: ---"
            tk.Label(scores_frame, text=score_text, font=("Arial", 11),
                    bg="#1a1a2e", fg="#ffffff").pack()
    
    def start_game(self, difficulty, time_limit):
        self.difficulty = difficulty
        self.time_limit = time_limit
        self.matches_found = 0
        self.moves = 0
        self.first_card = None
        self.second_card = None
        self.can_click = True
        
        # Setup game board
        self.clear_window()
        self.create_game_board()
        self.start_timer()
    
    def create_game_board(self):
        # Top bar
        top_frame = tk.Frame(self.root, bg="#16213e", height=70)
        top_frame.pack(fill=tk.X, pady=(0, 15))
        top_frame.pack_propagate(False)
        
        # Stats
        stats_frame = tk.Frame(top_frame, bg="#16213e")
        stats_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        self.timer_label = tk.Label(stats_frame, text=f"⏱️ Time: {self.time_limit}s", 
                                    font=("Arial", 14, "bold"), bg="#16213e", fg="#00ff00")
        self.timer_label.grid(row=0, column=0, padx=25)
        
        self.moves_label = tk.Label(stats_frame, text=f"🔄 Moves: {self.moves}", 
                                   font=("Arial", 14, "bold"), bg="#16213e", fg="#ffffff")
        self.moves_label.grid(row=0, column=1, padx=25)
        
        self.matches_label = tk.Label(stats_frame, text=f"✅ Pairs: {self.matches_found}/8", 
                                     font=("Arial", 14, "bold"), bg="#16213e", fg="#ffd700")
        self.matches_label.grid(row=0, column=2, padx=25)
        
        # Back button
        back_btn = tk.Button(top_frame, text="← Menu", font=("Arial", 11),
                           bg="#e74c3c", fg="white", command=self.show_main_menu,
                           cursor="hand2", width=10)
        back_btn.place(x=15, y=15)
        
        # Game grid container
        game_container = tk.Frame(self.root, bg="#1a1a2e")
        game_container.pack(expand=True, fill=tk.BOTH, pady=20)
        
        # Game frame centered
        game_frame = tk.Frame(game_container, bg="#1a1a2e")
        game_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
        
        # Create cards (4x4 grid = 16 cards = 8 pairs)
        selected_emojis = random.sample(self.emojis, 8)
        self.cards = selected_emojis * 2
        random.shuffle(self.cards)
        
        self.card_buttons = []
        for i in range(4):
            for j in range(4):
                idx = i * 4 + j
                btn = tk.Button(game_frame, text="?", font=("Arial", 36),
                              width=4, height=2, bg="#0f3460", fg="#ffffff",
                              command=lambda x=idx: self.card_clicked(x),
                              cursor="hand2", relief=tk.RAISED, bd=4)
                btn.grid(row=i, column=j, padx=10, pady=10)
                btn.emoji = self.cards[idx]
                btn.matched = False
                self.card_buttons.append(btn)
    
    def card_clicked(self, index):
        if not self.can_click or self.card_buttons[index].matched:
            return
        
        btn = self.card_buttons[index]
        
        if self.first_card is None:
            self.first_card = index
            btn.config(text=btn.emoji, bg="#e94560")
        elif self.second_card is None and index != self.first_card:
            self.second_card = index
            btn.config(text=btn.emoji, bg="#e94560")
            self.moves += 1
            self.moves_label.config(text=f"🔄 Moves: {self.moves}")
            self.can_click = False
            self.root.after(1000, self.check_match)
    
    def check_match(self):
        btn1 = self.card_buttons[self.first_card]
        btn2 = self.card_buttons[self.second_card]
        
        if btn1.emoji == btn2.emoji:
            # Match found
            btn1.matched = True
            btn2.matched = True
            btn1.config(bg="#27ae60", state=tk.DISABLED)
            btn2.config(bg="#27ae60", state=tk.DISABLED)
            self.matches_found += 1
            self.matches_label.config(text=f"✅ Pairs: {self.matches_found}/8")
            
            if self.matches_found == 8:
                self.game_won()
        else:
            # No match
            btn1.config(text="?", bg="#0f3460")
            btn2.config(text="?", bg="#0f3460")
        
        self.first_card = None
        self.second_card = None
        self.can_click = True
    
    def start_timer(self):
        self.start_time = time.time()
        self.timer_running = True
        self.update_timer()
    
    def update_timer(self):
        if not self.timer_running:
            return
        
        elapsed = int(time.time() - self.start_time)
        remaining = max(0, self.time_limit - elapsed)
        
        self.timer_label.config(text=f"⏱️ Time: {remaining}s")
        
        if remaining <= 10:
            self.timer_label.config(fg="#ff0000")
        
        if remaining <= 0:
            self.game_over()
        else:
            self.root.after(1000, self.update_timer)
    
    def game_won(self):
        self.timer_running = False
        
        # Update high score
        if self.moves < self.high_scores[self.difficulty]:
            self.high_scores[self.difficulty] = self.moves
            message = f"🎉 NEW RECORD! 🎉\n\nYou won in {self.moves} moves!\nDifficulty: {self.difficulty}"
        else:
            message = f"🎊 Congratulations! 🎊\n\nYou won in {self.moves} moves!\nDifficulty: {self.difficulty}"
        
        result = messagebox.askyesno("Victory!", message + "\n\nPlay again?")
        if result:
            self.start_game(self.difficulty, self.time_limit)
        else:
            self.show_main_menu()
    
    def game_over(self):
        self.timer_running = False
        self.can_click = False
        
        result = messagebox.askyesno("Time's Up!", 
                                    f"⏰ Time's up!\n\nYou found {self.matches_found}/8 pairs\nMoves: {self.moves}\n\nTry again?")
        if result:
            self.start_game(self.difficulty, self.time_limit)
        else:
            self.show_main_menu()
    
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryPuzzleGame(root)
    root.mainloop()
    