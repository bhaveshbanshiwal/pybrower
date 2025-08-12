import tkinter as tk
from tkinter import ttk

class TowerOfHanoi:
    def __init__(self, root):
        self.root = root
        self.canvas = tk.Canvas(root, width=400, height=400)  # Create canvas
        self.canvas.pack()
        self.draw_pegs()  # Now canvas exists, so this works

        
        self.disks = 3
        self.pegs = ['A', 'B', 'C']
        self.peg_positions = [150, 400, 650]
        self.disk_height = 30
        self.disk_width = 60
        
        self.selected_source = None
        self.selected_destination = None
        
        self.create_widgets()
        self.draw_pegs()
        self.draw_disks()

    def create_widgets(self):
        # Peg selection dropdowns
        self.source_var = tk.StringVar(value=self.pegs[0])
        self.dest_var = tk.StringVar(value=self.pegs[2])
        
        source_label = tk.Label(self.root, text="Source Peg:")
        source_label.pack(pady=5)
        source_menu = ttk.Combobox(self.root, textvariable=self.source_var, values=self.pegs)
        source_menu.pack(pady=5)
        
        dest_label = tk.Label(self.root, text="Destination Peg:")
        dest_label.pack(pady=5)
        dest_menu = ttk.Combobox(self.root, textvariable=self.dest_var, values=self.pegs)
        dest_menu.pack(pady=5)
        
        self.move_button = tk.Button(self.root, text="Move Disk", command=self.move_disk)
        self.move_button.pack(pady=10)

    def draw_pegs(self):
        for i in self.pegs:
            x = self.peg_positions[i]
            self.canvas.create_rectangle(
                x - 10, 550, x + 10, 50,
                fill="green", outline="black"
            )
            self.canvas.create_text(
                x, 580, text=peg, font=("Arial", 12)
            )

    def draw_disks(self):
        self.disks_on_pegs = {peg: [] for peg in self.pegs}
        for disk in range(self.disks, 0, -1):
            self.disks_on_pegs['A'].append(disk)
        
        self.canvas.delete("all")
        self.draw_pegs()
        
        for peg in self.pegs:
            disks = self.disks_on_pegs[peg]
            for i, disk in enumerate(disks):
                x = self.peg_positions[self.pegs.index(peg)]
                y = 550 - i * (self.disk_height + 5)
                
                # Calculate disk width based on size
                disk_size = self.disk_width + (self.disks - disk) * 10
                self.canvas.create_rectangle(
                    x - disk_size//2, y,
                    x + disk_size//2, y + self.disk_height,
                    fill="red", outline="black"
                )
                self.canvas.create_text(
                    x, y + self.disk_height//2, text=str(disk), font=("Arial", 12)
                )

    def move_disk(self):
        source = self.source_var.get()
        dest = self.dest_var.get()
        
        if source == dest:
            return
            
        if self.disks_on_pegs[source] and self.disks_on_pegs[dest]:
            top_source = self.disks_on_pegs[source][-1]
            top_dest = self.disks_on_pegs[dest][-1]
            
            if top_source > top_dest:
                return
                
        # Perform move
        if self.disks_on_pegs[source]:
            disk = self.disks_on_pegs[source].pop()
            self.disks_on_pegs[dest].append(disk)
            self.draw_disks()

if __name__ == "__main__":
    root = tk.Tk()
    app = TowerOfHanoi(root)
    root.mainloop()
