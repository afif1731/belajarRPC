# belajarRPC
Catatan: baru dicoba di ubuntu & vm generic/ubuntu2004
## Menyalakan Server
- Masuk ke folder `ini_server`
- buka terminal (ubuntu)
- jalankan `python3 ./erpc_server.py`
- Semua file yang diupload ke server disimpan di folder `shared`

## Send File ke Server
- Masuk ke folder `ini_client`
- buka terminal (ubuntu)
- jalankan `python3 ./erpc_client.py send [namafile]`

## Get File dari Server
- Masuk ke folder `ini_server`
- buka terminal (ubuntu)
- jalankan `python3 ./erpc_client.py get [namafile]`

## VM sebagai client
- Masuk ke folder `client_vm`
- buka terminal (ubuntu)
- jalankan `vagrant up`
- jalankan `vagrant ssh`
- jalankan fungsi python3 seperti pada bagian Get dan Send

