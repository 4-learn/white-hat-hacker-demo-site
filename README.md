# Falsk server XSS attack demonstration

## Installation
```bash=
pip3 install -r requirements.txt
```

## Run
```bash=
$ python3 server.py
```

## Reflected XSS (反射型 XSS)

#### 題目:
1. 請觸發 Alert windows
2. 請修補漏洞

#### 網址:
- /xss-attack-1

#### 解答:
- [Answer](https://github.com/yillkid/ntc-white-hat/tree/master/answer-xss-flask-server/001)

## Stored XSS (Inject)

#### 題目:
1. 請印出 `{"passoword":"myPasswordOhhh"}` 
2. 請修補漏洞

#### 網址:
- /inject

#### 解答:
- [Answer](https://github.com/yillkid/ntc-white-hat/tree/master/answer-xss-flask-server/002)

#### 題目:
1. 製造 SQL inject
2. 修補 bug

#### 網址:
- /is_admin

#### 題目情境:
- 某 postgresql 結構如下:
  - database 中「已經」存在一個 user table
  - user table 包含兩個 columns: username, admin
    - username: 代表該帳號的使用者名稱
    - admin: 代表該帳號權限，true 代表管理員, 反之就是 false
  - 根據這個 table, 也已經創建好兩筆資料
    - john (admin true)
    - mary (admin false)

- 某 python web service 如下
  - 請觀察範例中的 `/is_admin` 服務
  - 服務參數: username
  - 服務回傳值 (string) : Ture or False
  - 服務可帶入 username
  - 回傳值為是否為 admin 權限的字串 ( Ture / False ) 

#### 前期佈署:
1. 請在 Docker-Hub 中拉取 postgresql 建立 database container, 詳見 [Deploy Postgresql from Docker Hub](docs/deploy_db/README.md)

#### 測試:
- `http://127.0.0.1:5566/is_admin?username=john`
![is_admin_john](https://user-images.githubusercontent.com/185872/173305442-2bd9a510-057d-4032-85a0-f6bcfa5376e2.png)

- `http://127.0.0.1:5566/is_admin?username=mary`
![is_admin_mary](https://user-images.githubusercontent.com/185872/173305513-b8cd39db-ec2e-4375-a4cc-30f874f8b597.png)
