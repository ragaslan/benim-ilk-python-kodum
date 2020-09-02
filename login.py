name = input("adınızı bahşedermisiniz ? ")
hesapsoru = input("Hesap açmak istermisin {} ? E/H".format(name))
if hesapsoru == "E":
    username = input("Kendine bir kullanici adi yaz {} !".format(name))
    password = input("Kendine bir şifre belirle {} ama sakın unutma !".format(name))
    girissoru = input("Giriş Yapmak istermisin {} ? E/H ".format(name))
    if girissoru == "E":
        while(True):
            controlid = input("Kullanıcı adı:")
            controlpass = input("Sifre: ")
            if ((controlid == username) and (controlpass == password)):
                print("Artık Sistemdesin {} !".format(name))
                break
            elif ((controlid != username) and (controlpass == password)):
                print("Kullanıcı adında bir hata var {} !".format(name))
            elif ((controlid == username) and (controlpass != password)):
                print("Şifreni hatalı girdin {} !".format(name))
            else:
                print("Sen de kimsin be adam hiçbir bilgi doğru değil")
    elif girissoru == "H":
        print("Hesabın oluşturuldu ama sisteme girmek istemedin {}".format(name))
    else:
        print("Hatalı tuşlama yaptın {} lütfen seçeneklerine dikkat et!".format(name))

elif hesapsoru == "H":
    print("Sisteme hesap açmadığın için girilmedi {} !".format(name))
else:
    print("Hatalı tuşlama yaptın {} lütfen seçeneklerine dikkat et!".format(name))



