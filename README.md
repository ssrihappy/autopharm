## Autopharm V4
2024.7.1 Update
신한카드 간편결제 제한으로 인한 일반결제 자동화모듈  
키보드 보안 매핑은 직접 하셔야 합니다.




![](/Autopharm.gif)

### 오토팜(autopharm)_V1
대한민국 약국 약사들의 카드결제(카카오뱅크 신한카드)를 자동화 해 주는 파이썬 프로그램입니다.

<img src="/autopharm_exe.png"  width="200" height="200">

<img src="/results.jpg"  width="350" height="750">


공개된 코드는 누구나 수정해서 사용할 수 있으며 개인정보를 수집하지 않습니다. 

본인이 사용하고 있는 계정파일(Accounts.xlsx)이나 빌드된 exe 파일을 공유하는 것을 항상 주의하길 바랍니다.


현재 자동결제를 지원하는 프로그램은 아래와 같습니다.
1. 백제
2. 바로팜
3. 광동
4. 동아


프로그램은 정기적인 업데이트 및 사용자의 미숙으로 인한 오결제와 개인정보 유출을 책임지지 않으니 주의해서 사용하길 바랍니다.

## 설명서(How to Use)

1. Visual Studio Code 등 설치 : https://code.visualstudio.com/  

ref) https://crazykim2.tistory.com/748  

2. accounts.xlsx에 계정 정보 입력  

![](/accounts_1.png)

3. build.ipynb파일을 실행하여 exe 파일로 빌드  

![](/build.png)

정상적으로 실행이 완료되면 본인의 계정 및 카드정보가 저장된 자동 스크립트가 autopharm_v1.exe 파일로 생성됩니다.(클릭 시 자동결제 됨)

4. 카드결제가 필요할 때 exe 파일 실행(1일 1회) 혹은 윈도우 자동 스케줄러를 이용하여 자동 결제 시스템을 활용할 수 있음  

ref) https://rdsong.com/2219 - 윈도우 자동 스케줄러 참고 글















