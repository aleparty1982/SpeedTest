import speedtest
import tkinter as tk


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

if __name__ == "__main__":
    dl, ul, ping = test_speed()
    print(f"Download: {dl:.1f} Mb/s\nUpload: {ul:.1f} Mb/s\nPing: {ping:.0f} ms")
    
    root = tk.Tk()
    root.title("Speed Test")
    root.geometry("600x400")
    etichetta = tk.Label(
        master=root,
        text=f"Download: {dl:.1f} Mb/s\nUpload: {ul:.1f} Mb/s\nPing: {ping:.0f} ms",
        font=("Arial", 16),
        justify=tk.LEFT
    )
    etichetta.pack(
        padx=50,
        pady=50
    )
    
    root.mainloop()


