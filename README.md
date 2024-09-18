# Discord Botu ile SQLite ve SQLAlchemy

Bu proje, SQLAlchemy ile SQLite veritabanını kullanan ve temel ekleme, silme, güncelleme işlemleri yapabilen bir Discord botunu içerir. Proje, Python ve `discord.py` kütüphanesi kullanılarak geliştirilmiştir.

## Gereksinimler

Projenin çalışması için aşağıdaki Python kütüphanelerine ihtiyacınız olacak:

- `discord`
- `SQLAlchemy`

Bu kütüphaneleri yüklemek için, proje kök dizininde aşağıdaki komutu çalıştırabilirsiniz:

pip install -r requirements.txt

## Bot Komutları

!add_task <description> — açıklaması <description> olan bir görev ekler\n
!delete_task <task_id> — <task_id> tanımlayıcısına sahip görevi siler \n
!show_tasks — tüm görevlerin bir listesini gösterir\n
!complete_task <task_id> — <task_id> tanımlayıcısına sahip görevi tamamlandı olarak işaretler.\n

## Testler
Projedeki veri bağlantısı işlevinin test etmek için tests klasörlerindeki her bir dosyayı çalıştırabilirsiniz.
Test edilen veritabanı kayıtlarını tests klasöründeki tasks.db ile kontrol edebilirsiniz.



