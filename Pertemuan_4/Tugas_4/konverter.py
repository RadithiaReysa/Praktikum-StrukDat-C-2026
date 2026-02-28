from kurs import kurs

def konversi(dari, ke, jumlah):

    if dari == ke:
        return jumlah

    if dari == "IDR":
        return jumlah / kurs[ke]

    if ke == "IDR":
        return jumlah * kurs[dari]

    idr = jumlah * kurs[dari]
    return idr / kurs[ke]