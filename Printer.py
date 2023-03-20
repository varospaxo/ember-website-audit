
with open('./OutputFiles/Result_current.txt') as f:
    resultPing = f.readlines()
    print (resultPing)
with open('./OutputFiles/PortScannerFast_OP.txt') as f:
    resultPortscanner = f.readlines()
    print (resultPortscanner)
with open('./OutputFiles/Traceroute_OP.txt') as f:
    resultTraceroute = f.readlines()
    print (resultTraceroute)
with open('./OutputFiles/OSDetect_OP.txt') as f:
    resultOS = f.readlines()
    print (resultOS)
with open('./OutputFiles/SSLCert_OP.txt') as f:
    resultSSL = f.readlines()
    print (resultSSL)
with open('./OutputFiles/ReverseDNS_OP.txt') as f:
    resultDNS = f.readlines()
    print (resultDNS)
with open('./OutputFiles/Subdomain_OP.txt') as f:
    resultSubdomain = f.readlines()
    print (resultSubdomain)