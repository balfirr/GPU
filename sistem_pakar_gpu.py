import tkinter as tk
from tkinter import messagebox

class GPUSpecialistSystem:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistem Pakar Rekomendasi GPU")
        self.root.geometry("400x400")

        tk.Label(root, text="Pilih kebutuhan utama Anda:", font=("Helvetica", 14)).pack(pady=10)

        self.kebutuhan_vars = {
            "Gaming": tk.IntVar(),
            "Editing Video": tk.IntVar(),
            "Desain Grafis": tk.IntVar(),
            "Machine Learning": tk.IntVar(),
            "Budget Terbatas": tk.IntVar()
        }

        for kebutuhan, var in self.kebutuhan_vars.items():
            tk.Checkbutton(root, text=kebutuhan, variable=var).pack(anchor="w")

        tk.Button(root, text="Dapatkan Rekomendasi", command=self.rekomendasi_gpu).pack(pady=20)
        self.result_label = tk.Label(root, text="", wraplength=350, justify="left")
        self.result_label.pack()

    def rekomendasi_gpu(self):
        selected = [k for k, v in self.kebutuhan_vars.items() if v.get() == 1]

        if not selected:
            messagebox.showwarning("Peringatan", "Silakan pilih minimal satu kebutuhan.")
            return

        # Rules sederhana
        rekomendasi = []

        if "Gaming" in selected:
            if "Budget Terbatas" in selected:
                rekomendasi.append("Intel Arc B570 / AMD Radeon RX 6600")
            else:
                rekomendasi.append("NVIDIA RTX 4070 Ti Super / AMD Raden RX 7800 XT")

        if "Editing Video" in selected or "Desain Grafis" in selected:
            if "Budget Terbatas" in selected:
                rekomendasi.append("NVIDIA RTX 3060 8GB / AMD Radeon RX 6700")
            else:
                rekomendasi.append("NVIDIA RTX 4080 Ti Super / AMD Radeon RX 7900 XTX")
        if "Machine Learning" in selected:
            if "Budget Terbatas" in selected:
                rekomendasi.append("NVIDIA RTX 3060 12GB / AMD Radeon RX 6700 XT")
            else:
                rekomendasi.append("NVIDIA RTX 5090 / NVIDIA RTX 4090")

        if "Budget Terbatas" in selected and len(selected) == 1:
            rekomendasi.append("Intel Arc A380 / NVIDIA RTX 3050 6GB")

        # Hapus duplikat
        rekomendasi = list(set(rekomendasi))

        # Tampilkan hasil
        self.result_label.config(
            text="Rekomendasi GPU untuk Anda:\n- " + "\n- ".join(rekomendasi)
        )

if __name__ == "__main__":
    root = tk.Tk()
    app = GPUSpecialistSystem(root)
    root.mainloop()
