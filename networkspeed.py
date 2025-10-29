import speedtest
import tkinter as tk

dl_var = None
ul_var = None
ping_var = None
#n_test = 1 # numero di test da fare

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
    global dl_var, ul_var, ping_var, valore_input
    
    dl_tot = 0
    ul_tot = 0
    ping_tot = 0
    
    try:
        n_test = int(valore_input.get())
    except ValueError:
        error_window('Inserire un numero!')
    else:

        for _ in range(n_test):
            dl_i, ul_i, ping_i = test_speed()
            print(dl_i, ul_i, ping_i)
            print('\n')
            dl_tot += dl_i
            ul_tot += ul_i
            ping_tot += ping_i
        
        dl = dl_tot / n_test
        ul = ul_tot / n_test
        ping = ping_tot / n_test

        #dl, ul, ping = test_speed()

        dl_var.set(f"Download Speed: {dl:.1f} Mb/s")
        ul_var.set(f"Upload Speed: {ul:.1f} Mb/s")
        ping_var.set(f"Ping: {int(ping)} ms")

        print("Programma terminato")

def error_window(messaggio: str):
    win_error = tk.Tk()
    win_error.title("Errore")
    win_error.geometry("300x200")
    errore = tk.Label(
        master=win_error,
        text=messaggio
    ).pack()
    win_error.focus_force()
    win_error.mainloop()

if __name__ == "__main__":
    
    # Inizializzo la finestra
    root = tk.Tk()
    root.title("Speed Test")
    root.geometry("400x250")
    #root.attributes('-topmost', True) # se lo volessi SEMPRE in primo piano
    
    # Inizializzo le variabili tkinter
    dl_var = tk.StringVar(value="Download Speed: N/A")
    ul_var = tk.StringVar(value="Upload Speed: N/A")
    ping_var = tk.StringVar(value="Ping: N/A")
    valore_input = tk.StringVar()

    # Valore di default
    valore_input.set('1')

    # Descrizione cella di input
    descr_input = tk.Label(
        master=root,
        text='Inserire il numero di speed test da fare',
        font=('Arial', 20)
    ).grid(row=0, column=0)

    # Cella di input del numero di test
    casella_input = tk.Entry(
        master=root,
        textvariable=valore_input,
        width=2
    ).grid(row=0, column=1, sticky=tk.S)

    # Bottone di avvio della funzione
    # Deve richiamare la funzione che fa il refresh dei valori di testo
    bottone_avvio = tk.Button(
        master=root,
        text="Avvia lo Speed Test",
        command=refresh_values
    ).grid(row=1, column=0, columnspan=2, sticky='ew', pady=10)

    # Etichette dei tre valori
    # Usano textvariable collegato alla variabile tkinter
    etichetta_dl = tk.Label(
        master=root,
        textvariable=dl_var,
        font=("Arial", 16)
    ).grid(row=2, column=0, sticky=tk.W)

    etichetta_ul = tk.Label(
        master=root,
        textvariable=ul_var,
        font=("Arial", 16)
    ).grid(row=3, column=0, sticky=tk.W)

    etichetta_ping = tk.Label(
        master=root,
        textvariable=ping_var,
        font=("Arial", 16)        
    ).grid(row=4, column=0, sticky=tk.W)
    
    #print("Programma terminato")

    root.focus_force() # forza in primo piano all'apertura
    root.mainloop()


