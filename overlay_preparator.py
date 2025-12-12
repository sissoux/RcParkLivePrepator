import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

class OverlayPreparator:
    def __init__(self, root):
        self.root = root
        self.root.title("RC Park Live Overlay Preparator")
        self.root.geometry("600x450")
        
        # File path variables
        self.file_paths = {
            'ScreenPodiumVide': tk.StringVar(),
            'ScreenRanking': tk.StringVar(),
            'ScreenStartLiveVide': tk.StringVar(),
            'BandeauSeul': tk.StringVar(),
            'ScreenPodiumVide_interview': tk.StringVar(),
            'ScreenRanking_interview': tk.StringVar(),
            'ScreenStartLiveVide_interview': tk.StringVar()
        }
        
        # Output folder variable
        self.output_folder = tk.StringVar(value="c:/RCPARK_Live/CurrentRace/OverlayAssets")
        
        # Create UI
        self.create_widgets()
    
    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root, text="RC Park Live Overlay Preparator", 
                               font=("Arial", 14, "bold"))
        title_label.pack(pady=10)
        
        # File selection frame
        frame = tk.Frame(self.root)
        frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        row = 0
        for name in self.file_paths.keys():
            # Label
            label = tk.Label(frame, text=f"{name}:", width=20, anchor="w")
            label.grid(row=row, column=0, padx=5, pady=5, sticky="w")
            
            # Entry
            entry = tk.Entry(frame, textvariable=self.file_paths[name], width=35)
            entry.grid(row=row, column=1, padx=5, pady=5)
            
            # Browse button
            btn = tk.Button(frame, text="Browse", 
                           command=lambda n=name: self.browse_file(n))
            btn.grid(row=row, column=2, padx=5, pady=5)
            
            row += 1
        
        # Output folder section
        output_label = tk.Label(frame, text="Output Folder:", width=20, anchor="w")
        output_label.grid(row=row, column=0, padx=5, pady=5, sticky="w")
        
        output_entry = tk.Entry(frame, textvariable=self.output_folder, width=35)
        output_entry.grid(row=row, column=1, padx=5, pady=5)
        
        output_btn = tk.Button(frame, text="Browse", 
                              command=self.browse_output_folder)
        output_btn.grid(row=row, column=2, padx=5, pady=5)
        
        # Generate button
        generate_btn = tk.Button(self.root, text="Generate", 
                                command=self.generate_overlays,
                                bg="#4CAF50", fg="white", 
                                font=("Arial", 12, "bold"),
                                padx=20, pady=10)
        generate_btn.pack(pady=20)
    
    def browse_file(self, name):
        filename = filedialog.askopenfilename(
            title=f"Select {name}",
            filetypes=[("Image files", "*.png *.jpg *.jpeg *.bmp *.tiff"), 
                      ("All files", "*.*")]
        )
        if filename:
            self.file_paths[name].set(filename)
    
    def browse_output_folder(self):
        folder = filedialog.askdirectory(
            title="Select Output Folder",
            initialdir=self.output_folder.get()
        )
        if folder:
            self.output_folder.set(folder)
    
    def resize_image(self, image_path, output_name, output_folder):
        """Resize image to fit 1920x1080 while maintaining aspect ratio"""
        try:
            # Open image
            img = Image.open(image_path)
            
            # Convert to RGBA to preserve alpha channel
            if img.mode != 'RGBA':
                img = img.convert('RGBA')
            
            # Get current dimensions
            width, height = img.size
            aspect_ratio = width / height
            target_ratio = 16 / 9
            
            # Calculate new dimensions
            if aspect_ratio > target_ratio:
                # Width is the limiting factor
                new_width = 1920
                new_height = int(1920 / aspect_ratio)
            else:
                # Height is the limiting factor
                new_height = 1080
                new_width = int(1080 * aspect_ratio)
            
            # Resize image with high-quality resampling
            resized_img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)
            
            # Create output folder if it doesn't exist
            os.makedirs(output_folder, exist_ok=True)
            
            # Save with new name
            output_path = os.path.join(output_folder, f"{output_name}-1080.png")
            resized_img.save(output_path, "PNG")
            
            return output_path
        except Exception as e:
            raise Exception(f"Error processing {output_name}: {str(e)}")
    
    def generate_overlays(self):
        try:
            # Check if all files are selected
            missing_files = []
            for name, var in self.file_paths.items():
                if not var.get():
                    missing_files.append(name)
            
            if missing_files:
                messagebox.showwarning("Missing Files", 
                                      f"Please select files for:\n" + "\n".join(missing_files))
                return
            
            # Process each image
            output_folder = self.output_folder.get()
            processed_files = []
            for name, var in self.file_paths.items():
                file_path = var.get()
                if not os.path.exists(file_path):
                    messagebox.showerror("Error", f"File not found: {file_path}")
                    return
                
                # Replace underscore with hyphen in interview file names
                output_name = name.replace('_interview', '-interview')
                output_path = self.resize_image(file_path, output_name, output_folder)
                processed_files.append(output_path)
            
            # Success message
            messagebox.showinfo("Success", 
                              f"Successfully processed {len(processed_files)} images!\n\n" +
                              "Output files:\n" + "\n".join([os.path.basename(f) for f in processed_files]))
            
        except Exception as e:
            messagebox.showerror("Error", str(e))

def main():
    root = tk.Tk()
    app = OverlayPreparator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
