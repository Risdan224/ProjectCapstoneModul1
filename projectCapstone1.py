# Daftar Menu Utama Program
menuUtama = ['1. Report Data Karyawan', 
                '2. Menambahkan Data Karyawan', 
                '3. Mengubah Data Karyawan', 
                '4. Menghapus Data Karyawan', 
                '0. Keluar Menu']

# Daftar Kolom/Keterangan Data Karyawan
kolomData = ['nik','nama','jabatan','gender','status']

# Data Dummy Karyawan
daftarKaryawan = []
daftarKaryawan.append({
    'NIK':'BUBL01',
    'Nama':'Joko Susilo', 
    'Jabatan':'Mandor Bengkel', 
    'Gender':'L', 
    'Status':'M'})
daftarKaryawan.append({
    'NIK':'BUBL02',
    'Nama':'Fitriana', 
    'Jabatan':'Krani Bengkel', 
    'Gender':'P', 
    'Status':'BM'})

# Fungsi Membaca Data Karyawan
def readData(daftarKaryawan):
    while True:
        print('==============================================================================')
        print('1. Report Seluruh Data')
        print('2. Report Data Tertentu')
        print('0. Kembali ke Menu Utama')
        inputRead = int(input('Silahkan Pilih Sub-menu Report Data: '))
        if inputRead == 1:
            print('==============================================================================')
            if any(daftarKaryawan) == False:
                print('Tidak Ada Data Karyawan Tersimpan!')
            else:
                for data in daftarKaryawan:
                    print(f"NIK : {data['NIK']}, Nama : {data['Nama']}, Jabatan : {data['Jabatan']}, Gender : {data['Gender']}, Status : {data['Status']}")
        elif inputRead == 2:
            inputNIK = input('Masukkan NIK Karyawan: ')
            checkData = []
            for data in daftarKaryawan:
                NIK = data['NIK']
                if NIK.lower() == inputNIK.lower():
                    print('==============================================================================')
                    print(f"NIK : {data['NIK']}, Nama : {data['Nama']}, Jabatan : {data['Jabatan']}, Gender : {data['Gender']}, Status : {data['Status']}")
                    checkData.append(NIK)
            if any(checkData) == False:
                print('==============================================================================')
                print('Data Tidak Ditemukan!')
        
        elif inputRead == 0:
            break
        else:
            print('Pilihan Menu Tidak Tersedia')
# Fungsi Membuat Data Karyawan Baru
def createData(daftarKaryawan):
    dataBaru = []
    while True:
        print('==============================================================================')
        print('1. Tambah Data Karyawan')
        print('0. Kembali ke Menu Utama')
        inputAdd = int(input('Silahkan Pilih Sub-menu Create Data: '))
        if inputAdd == 1:
            print('==============================================================================')
            NIKBaru = input('Masukkan NIK Karyawan: ')
            checkData = []
            for data in daftarKaryawan:
                NIK = data['NIK']
                if NIK.lower() == NIKBaru.lower():
                    checkData.append(NIK)
            
            if any(checkData) == True:
                print('Data Sudah Ada!')
            else:
                namaBaru = input('Masukkan Nama Karyawan: ')
                jabatanBaru = input('Masukkan Jabatan Karyawan: ')
                genderBaru = input('Masukkan Gender Karyawan (L/P): ')
                statusBaru = input('Masukkan Status Karyawan (BM/M): ')
                dataBaru = {
                    'NIK':NIKBaru,
                    'Nama':namaBaru, 
                    'Jabatan':jabatanBaru, 
                    'Gender':genderBaru, 
                    'Status':statusBaru
                }
                while True:
                    dataOk = input('Apakah Data akan Disimpan (Y/N): ')
                    if dataOk == 'Y':
                        daftarKaryawan.append(dataBaru)
                        break
                    elif dataOk == 'N':
                        break
        elif inputAdd == 0:
            break
        else:
            print('Pilihan Menu Tidak Tersedia')
# Fungsi Mengubah Data Karyawan
def changeData(daftarKaryawan):
    while True:
        print('==============================================================================')
        print('1. Ubah Data Karyawan')
        print('0. Kembali ke Menu Utama')
        inputChange = int(input('Silahkan Pilih Sub-menu Update Data: '))
        if inputChange == 1:
            print('==============================================================================')
            NIKUbah = input('Masukkan NIK: ')
            checkData = []
            for i in range(len(daftarKaryawan)):
                data = daftarKaryawan[i]
                NIK = data['NIK']
                if NIK.lower() == NIKUbah.lower():
                    print(f"NIK : {data['NIK']}, Nama : {data['Nama']}, Jabatan : {data['Jabatan']}, Gender : {data['Gender']}, Status : {data['Status']}")
                    # Inserting to checkdata
                    checkData.append(NIK)
                    # Continue asking for update data
                    while True:
                        dataOk = input('Apakah Akan Mengubah Data Tersebut (Y/N)?: ')
                        if dataOk == 'Y':
                            checkData2 = []
                            while True:
                                dataEdit = input('Masukkan Kolom/Keterangan yang Ingin diubah: ')
                                for data2 in kolomData:
                                    if data2 == dataEdit.lower():
                                        checkData2.append(dataEdit.lower())
                                        break
                                if any(checkData2) == False:
                                    print('Kolom Tidak Tersedia')
                                else:
                                    break
                            # Correcting name of coloumn
                            if checkData2[0] == 'nik':
                                checkData2[0] = 'NIK'
                            else:
                                checkData2[0] = checkData2[0].title()
                            
                            dataBaru = input(f'Masukkan {checkData2[0]} baru: ')
                            while True:
                                dataOkEdit = input('Apakah Data akan diubah?(Y/N): ')
                                if dataOkEdit == 'Y':
                                    daftarKaryawan[i][checkData2[0]] = dataBaru
                                    print('Data diubah!')
                                    break
                                if dataOkEdit == 'N':
                                    print('Data tidak diubah!')
                                    break
                            break
                        elif dataOk == 'N':
                            break     
            if any(checkData) == False:
                print('Data Tidak Tersedia!')

        elif inputChange == 0:
            break
        else:
            print('Pilihan Menu Tidak Tersedia')
# Fungsi Menghapus Data Karyawan
def deleteData(daftarKaryawan):
    while True:
        print('==============================================================================')
        print('1. Hapus Data Karyawan')
        print('0. Kembali ke Menu Utama')
        inputDelete = int(input('Silahkan Pilih Sub-menu Delete Data: '))
        if inputDelete == 1:
            print('==============================================================================')
            NIKHapus = input('Masukkan NIK: ')
            checkData = []
            index = -1
            for i in range(len(daftarKaryawan)):
                data = daftarKaryawan[i]
                NIK = data['NIK']
                if NIK.lower() == NIKHapus.lower():
                    print(f"NIK : {data['NIK']}, Nama : {data['Nama']}, Jabatan : {data['Jabatan']}, Gender : {data['Gender']}, Status : {data['Status']}")
                    # Inserting to checkdata
                    checkData.append(NIK)
                    # Continue asking for delete
                    while True:
                        dataOk = input('Apakah Akan Menghapus Data Tersebut (Y/N)?: ')
                        if dataOk == 'Y':
                            index = i
                            print('Data Terhapus')
                            break
                        elif dataOk == 'N':
                            print('Data Tidak Dihapus')
                            break     
            if any(checkData) == False:
                print('Data Tidak Tersedia!')
            if index != -1:
                del daftarKaryawan[index]    
        elif inputDelete == 0:
            break
        else:
            print('Pilihan Menu Tidak Tersedia')

# Menu Utama
while True:
    print('========= Data Record Karyawan PT Maju Mundur Merdeka ===========')
    for i in menuUtama:
        print(i)

    # Meminta Pilihan Menu dari User
    inputUser = int(input('Silahkan Pilih Menu = '))
    if inputUser == 1:
        readData(daftarKaryawan)
    elif inputUser == 2:
        createData(daftarKaryawan)
    elif inputUser == 3:
        changeData(daftarKaryawan)
    elif inputUser == 4:
        deleteData(daftarKaryawan)
    elif inputUser == 0:
        break
    else:
        print('Pilihan Menu Tidak Tersedia!')
        print('\n')