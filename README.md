# stock-tools

주식 관련 주요 정보를 크롤링 하는 tool 입니다.

| OS | Tested |
| - | - |
| Ubuntu 18.04 | O |
| Windows | X |
| Mac | X |

## 사전 준비

### Google Chrome 브라우저 설치

[공식 홈페이지](https://www.google.com/intl/ko/chrome/)에서 브라우저 다운로드 및 설치

### Chrome Driver 다운로드

아래와 같이 브라우저 버전을 확인 후,
```bash
google-chrome --version
```

```bash
# 출력 예
Google Chrome 101.0.4951.64 
```

Chrome Webdriver [다운로드 페이지](https://chromedriver.storage.googleapis.com/index.html)에서 앞의 세자리 (예: 101.0.4951) 가 동일한 드라이버를 driver 디렉토리에 다운로드 하고 압축을 해지 합니다.

```bash
# 예) 101.0.4951.41 버전 Linux 64 bit OS 용으로 다운로드 받을 경우
wget https://chromedriver.storage.googleapis.com/101.0.4951.41/chromedriver_linux64.zip
unzip chromedriver_linux64.zip
mv chromedriver driver/
rm chromedriver_linux64.zip
```
