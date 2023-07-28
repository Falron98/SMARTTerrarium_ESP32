from WIFIconnect import show_hotspot_ip


def stop_ftp():
    
    from ftp_serv import uftpd
    uftpd.stop()
    
async def start_ftp():
    
    from ftp_serv import uftpd