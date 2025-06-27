from services.XupiscShort import XupiscShort
from services.XupiscQrcode import XupiscQrcode
from services.XupiscRegister import XupiscRegister

def main():
    input("Bem vindo ao Xupisc URL Shortener!\nPressione Enter para continuar...\n")
    print("Gerando URL curta e QR Code...\n")

    sair = 'n'
    while sair != 's':
        url = input("Informar a URL que deseja encurtar: ")

        # gerando URL curta e QR Code
        shortner = XupiscShort(url)
        shortner.generate_short_url()
        print(f"URL curta gerada com sucesso: {shortner.short_url}")
        print("Gerando QR Code...\n")
        linkqrcode = XupiscQrcode(shortner).generate_qrcode()
        print(f"QR Code gerado com sucesso! Salvo em: {linkqrcode}")

        #Registrando no redis
        xupisc_register = XupiscRegister()
        if xupisc_register.url_exists(shortner.short_url) == False:
            xupisc_register.register_url(shortner.short_url, url, linkqrcode)

        sair = input("\nDeseja sair? (s/n): ").strip().lower()

    print("Obrigado por usar o Xupisc URL Shortener!\n")
    input("Pressione Enter para sair...")

if __name__ == "__main__":
    main()