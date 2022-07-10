# stockutils

한국 주식 관련 주요 정보를 크롤링 하는 tool 입니다.

| OS           | Tested |
| ------------ | ------ |
| Ubuntu 20.04 | O      |

## 사전 준비

### Google Chrome 브라우저 설치

[공식 홈페이지](https://www.google.com/intl/ko/chrome/)에서 다운로드 및 설치를 할 수 있습니다.

### Install wget, selenium, webdriver-manager
```bash
sudo apt install python3-pip wget
pip3 install selenium webdriver-manager
```

## 한국

### 주식 목록 가져오기

아래 명령을 통해 한국 거래소 페이지에서 일반 주식, ETF, ETN 리스트 정보를 다운로드 받을 수 있습니다.

> **주의**
> 
> `$HOME/Downloads` 디렉토리에 data_*.csv 패턴의 파일이 있다면 삭제 확인 프롬프트가 화면에 표시되며, `y` 를 눌러야 진행됩니다.

```bash
python3 ./kr/list.py 
```

결과적으로 아래와 같은 파일이 생성됩니다.

| 파일         | 내용           |
| ------------ | -------------- |
| kr-stock.csv | 한국 일반 주식 |
| kr-etf.csv   | 한국 ETF       |
| kr-etn.csv   | 한국 ETN       |

## 미국

### 주식 목록 가져오기

아래 명령을 통해 "Ticker,회사이름" 으로 구성된 미국 주식 리스트를 다운로드 받을 수 있습니다.

```bash
./us/list.sh
```

결과적으로 `us-stock.csv` 파일이 생성됩니다.