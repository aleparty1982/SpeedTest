import speedtest
import tkinter as tk

dl_var = None
ul_var = None
ping_var = None

def mbit_conversion(bits):
    return bits / 1024 / 1024

def test_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    dl = mbit_conversion(st.download())
    ul = mbit_conversion(st.upload())
    ping = st.results.ping
    #print(f"Download: {dl:.1f} Mb/s\nUpload: {ul:.1f} Mb/s\nPing: {ping:.0f} ms")
    return dl, ul, ping

def refresh_values():
    global dl_var, ul_var, ping_var
    
    dl, ul, ping = test_speed()
    
    dl_var.set(f"Download Speed: {dl:.1f} Mb/s")
    ul_var.set(f"Upload Speed: {ul:.1f} Mb/s")
    ping_var.set(f"Ping: {int(ping)} ms")

    #print(f"Download: {dl:.1f} Mb/s\nUpload: {ul:.1f} Mb/s\nPing: {ping:.0f} ms")

if __name__ == "__main__":
    #dl, ul, ping = test_speed()
    #print(f"Download: {dl:.1f} Mb/s\nUpload: {ul:.1f} Mb/s\nPing: {ping:.0f} ms")
    
    root = tk.Tk()
    root.title("Speed Test")
    root.geometry("300x150")
    #root.attributes('-topmost', True)
    
    dl_var = tk.StringVar(value="Download Speed: N/A")
    ul_var = tk.StringVar(value="Upload Speed: N/A")
    ping_var = tk.StringVar(value="Ping: N/A")

    bottone_avvio = tk.Button(
        master=root,
        text="Avvia lo Speed Test",
        command=refresh_values
    ).pack(padx=5, pady=5)

    etichetta_dl = tk.Label(
        master=root,
        textvariable=dl_var,
        font=("Arial", 16),
        justify=tk.LEFT
    ).pack(padx=5, pady=5)

    etichetta_ul = tk.Label(
        master=root,
        textvariable=ul_var,
        font=("Arial", 16),
        justify=tk.LEFT
    ).pack(padx=5, pady=5)

    etichetta_ping = tk.Label(
        master=root,
        textvariable=ping_var,
        font=("Arial", 16),
        justify=tk.LEFT
    ).pack(padx=5, pady=5)

    #root.lift()
    root.focus_force()
    root.mainloop()


