import tkinter as tk
from tkinter import ttk, messagebox
from core.script_gen import generate_script_with_gpt, generate_random_script
from core.video_gen import generate_video_from_script

class ReelAutoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("ReelAuto - YouTube Shorts Generator")
        self.root.geometry("600x500")
        self.root.resizable(False, False)

        self.topic_var = tk.StringVar()

        # === UI Components ===
        self.create_widgets()

    def create_widgets(self):
        title = ttk.Label(self.root, text="🎬 ReelAuto", font=("Helvetica", 20, "bold"))
        title.pack(pady=10)

        subtitle = ttk.Label(self.root, text="Generate YouTube Shorts Scripts with AI", font=("Helvetica", 12))
        subtitle.pack(pady=5)

        topic_label = ttk.Label(self.root, text="Enter a Topic:")
        topic_label.pack(pady=(20, 5))

        topic_entry = ttk.Entry(self.root, textvariable=self.topic_var, font=("Helvetica", 12), width=40)
        topic_entry.pack()

        # === Buttons in a single row ===
        button_frame = ttk.Frame(self.root)
        button_frame.pack(pady=20)

        generate_button = ttk.Button(button_frame, text="Generate Script", command=self.on_generate_script)
        generate_button.grid(row=0, column=0, padx=5)

        generate_video_button = ttk.Button(button_frame, text="Generate Video", command=self.on_generate_video)
        generate_video_button.grid(row=0, column=1, padx=5)

        save_script_button = ttk.Button(button_frame, text="Save Script", command=self.on_save_script)
        save_script_button.grid(row=0, column=2, padx=5)

        clear_button = ttk.Button(button_frame, text="Clear Output", command=self.on_clear_output)
        clear_button.grid(row=0, column=3, padx=5)

        # Output display
        self.output_text = tk.Text(self.root, wrap=tk.WORD, font=("Helvetica", 12))
        self.output_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

    def on_generate_script(self):
        topic = self.topic_var.get().strip()
        if not topic:
            messagebox.showerror("Missing Topic", "Please enter a topic.")
            return

        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, "Generating script... Please wait.\n")

        try:
            script = generate_script_with_gpt(topic)
        except Exception as e:
            script = f"[Error: {str(e)}]"

        self.output_text.delete(1.0, tk.END)
        self.output_text.insert(tk.END, script)

    def on_generate_video(self):
        script = self.output_text.get("1.0", tk.END).strip()  # Use self.output_text here

        if not script:
            messagebox.showwarning("Empty Script", "Please generate a script first.")
            return

        try:
            print("Generating video... Please wait.")
            output_path = generate_video_from_script(script)
            print("✅ Video generated at:", output_path)
            messagebox.showinfo("Success", f"Video generated successfully!\n\nSaved to:\n{output_path}")
        except Exception as e:
            print("❌ Video generation failed:", e)
            messagebox.showerror("Error", f"Video generation failed:\n\n{e}")

    def on_save_script(self):
        script = self.output_text.get(1.0, tk.END).strip()  # Get the script from the output_text widget
        if not script:
            messagebox.showerror("No Script", "Please generate a script first.")
            return

        # Save the script to a file
        try:
            with open("generated_script.txt", "w") as file:
                file.write(script)
            messagebox.showinfo("Success", "Script saved successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save script: {str(e)}")

    def on_clear_output(self):
        self.output_text.delete(1.0, tk.END)
