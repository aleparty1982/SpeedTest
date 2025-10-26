import speedtest
import tkinter as tk

dl_var = None
ul_var = None
ping_var = None

def mbit_conversion(bits): 
    '''
    converte da bit/s a Mbit/s
    '''
    return bits / 1024 / 1024

def test_speed():
    '''
    ritorna velocità di download, upload e ping
    '''
    st = speedtest.Speedtest()
    st.get_best_server()
    dl = mbit_conversion(st.download())
    ul = mbit_conversion(st.upload())
    ping = st.results.ping
    #print(f"Download: {dl:.1f} Mb/s\nUpload: {ul:.1f} Mb/s\nPing: {ping:.0f} ms")
    return dl, ul, ping

def refresh_values():
    '''
    Fa il refresh dei valori di download, upload e ping, richiamando la funzione test_speed()
    Setta le variabili di testo da usare nell'interfaccia tkinter
    '''
    global dl_var, ul_var, ping_var
    
    dl, ul, ping = test_speed()
    
    dl_var.set(f"Download Speed: {dl:.1f} Mb/s")
    ul_var.set(f"Upload Speed: {ul:.1f} Mb/s")
    ping_var.set(f"Ping: {int(ping)} ms")

if __name__ == "__main__":
    
    # Inizializzo la finestra
    root = tk.Tk()
    root.title("Speed Test")
    root.geometry("300x150")
    #root.attributes('-topmost', True) # se lo volessi SEMPRE in primo piano
    
    # Inizializzo le variabili tkinter
    dl_var = tk.StringVar(value="Download Speed: N/A")
    ul_var = tk.StringVar(value="Upload Speed: N/A")
    ping_var = tk.StringVar(value="Ping: N/A")

    # Bottone di avvio della funzione
    # Deve richiamare la funzione che fa il refresh dei valori di testo
    bottone_avvio = tk.Button(
        master=root,
        text="Avvia lo Speed Test",
        command=refresh_values
    ).pack(padx=5, pady=5)

    # Etichette dei tre valori
    # Usano textvariable collegato alla variabile tkinter
    etichetta_dl = tk.Label(
        master=root,
        textvariable=dl_var,
        font=("Arial", 16)
    ).pack(padx=5, pady=5, anchor=tk.W)

    etichetta_ul = tk.Label(
        master=root,
        textvariable=ul_var,
        font=("Arial", 16)
    ).pack(padx=5, pady=5, anchor=tk.W)

    etichetta_ping = tk.Label(
        master=root,
        textvariable=ping_var,
        font=("Arial", 16)        
    ).pack(padx=5, pady=5, anchor=tk.W)
    
    root.focus_force() # forza in primo piano all'apertura
    root.mainloop()


