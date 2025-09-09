import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from database import criar_tabela, buscar_listas, buscar_por_lista
from utils import importar_csv

class RankingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎮 Sistema de Ranking de Jogadores")
        self.root.geometry("750x500")
        self.root.resizable(False, False)

        # Título
        titulo = ttk.Label(root, text="🏆 Ranking de Jogadores", font=("Segoe UI", 16, "bold"))
        titulo.pack(pady=10)

        # Frame principal dividido
        frame = ttk.Frame(root, padding=10)
        frame.pack(fill="both", expand=True)

        # Menu lateral
        menu_frame = ttk.Frame(frame)
        menu_frame.pack(side="left", fill="y", padx=10)

        btn_importar = ttk.Button(menu_frame, text="📂 Importar CSV", width=20, command=self.importar_csv)
        btn_importar.pack(pady=10)

        btn_listas = ttk.Button(menu_frame, text="📊 Exibir Ranking", width=20, command=self.exibir_listas)
        btn_listas.pack(pady=10)

        btn_sair = ttk.Button(menu_frame, text="❌ Sair", width=20, command=root.quit)
        btn_sair.pack(pady=10)

        # Área de exibição
        display_frame = ttk.Frame(frame)
        display_frame.pack(side="right", fill="both", expand=True)

        # Scrollbar + área de texto
        scrollbar = ttk.Scrollbar(display_frame)
        scrollbar.pack(side="right", fill="y")

        self.text_area = tk.Text(
            display_frame,
            height=20,
            width=70,
            state="disabled",
            wrap="none",
            font=("Consolas", 11)
        )
        self.text_area.pack(fill="both", expand=True)
        self.text_area.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.text_area.yview)

    def importar_csv(self):
        arquivo = filedialog.askopenfilename(
            title="Selecione o arquivo CSV",
            filetypes=[("CSV files", "*.csv")]
        )
        if arquivo:
            try:
                lista_id = len(buscar_listas()) + 1  # cria nova lista automaticamente
                importar_csv(arquivo, lista_id)
                messagebox.showinfo("Sucesso", f"✅ Dados importados para a lista {lista_id}!")
            except Exception as e:
                messagebox.showerror("Erro", f"❌ Falha ao importar CSV:\n{e}")

    def exibir_listas(self):
        listas = buscar_listas()
        if not listas:
            messagebox.showwarning("Aviso", "Nenhuma lista encontrada!")
            return

        # Criar janela para escolher lista
        lista_win = tk.Toplevel(self.root)
        lista_win.title("Escolher Lista de Ranking")
        lista_win.geometry("300x150")
        lista_win.resizable(False, False)

        ttk.Label(lista_win, text="Selecione uma lista:", font=("Segoe UI", 11)).pack(pady=10)

        combo = ttk.Combobox(lista_win, values=listas, state="readonly")
        combo.pack(pady=5)
        combo.current(0)

        def mostrar_ranking():
            lista_id = combo.get()
            jogadores = buscar_por_lista(lista_id)
            if jogadores:
                self.mostrar_ranking(jogadores, lista_id)
            else:
                messagebox.showinfo("Info", "Nenhum jogador nessa lista.")
            lista_win.destroy()

        ttk.Button(lista_win, text="Mostrar", command=mostrar_ranking).pack(pady=10)

    def mostrar_ranking(self, jogadores, lista_id):
        self.text_area.config(state="normal")
        self.text_area.delete("1.0", tk.END)

        self.text_area.insert(tk.END, f"===== RANKING (Lista {lista_id}) =====\n\n")
        for i, (nome, nivel, pontuacao) in enumerate(jogadores, start=1):
            if i == 1:
                destaque = "🥇"
            elif i == 2:
                destaque = "🥈"
            elif i == 3:
                destaque = "🥉"
            else:
                destaque = "-"
            self.text_area.insert(tk.END, f"{destaque} {i}º | {nome:<15} | Nível {nivel:<3} | Pontuação {pontuacao}\n")

        self.text_area.config(state="disabled")

if __name__ == "__main__":
    criar_tabela()
    root = tk.Tk()
    app = RankingApp(root)
    root.mainloop()
