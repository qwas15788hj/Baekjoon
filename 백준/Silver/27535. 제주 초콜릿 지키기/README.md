# [Silver IV] 제주 초콜릿 지키기 - 27535 

[문제 링크](https://www.acmicpc.net/problem/27535) 

### 성능 요약

메모리: 111608 KB, 시간: 132 ms

### 분류

구현, 수학, 정렬

### 제출 일자

2025년 7월 14일 10:41:58

### 문제 설명

<p>지난 주에 제주도에 다녀온 선생님은 냉장고에 제주 초콜릿을 숨겨두고 몰래 먹고 있다. </p>

<p style="text-align: center;"><img alt="" src=""></p>

<p style="text-align: center;">사진 1. 실제 선생님의 냉장고 안을 찍은 사진 </p>

<p>눈치가 빠른 학생들은 선생님의 초콜릿을 훔쳐 먹었다! 이를 알아챈 선생님은 포스트잇에 현재 초콜릿의 남은 개수를 적어 놓아 학생들이 먹는 일이 없도록 하려고 한다. 다만, 이 숫자를 학생들이 바꿔버릴 수 있기 때문에 특정한 규칙으로 초콜릿의 개수를 적으려고 한다.</p>

<p>초콜릿의 종류는 총 5개 있으며 각각 한라봉(<code>H</code>), 감귤(<code>T</code>), 백년초(<code>C</code>), 키위(<code>K</code>), 녹차(<code>G</code>)이다.</p>

<p>남은 초콜릿의 개수를 적는 규칙은 다음과 같다.</p>

<ol>
	<li>첫 번째 줄에 남아있는 초콜릿의 총 개수를 적고, 바로 뒤에 <code>7H</code> (<code>개</code>를 아스키 문자로 형상화한 단어)를 적는다.

	<ul>
		<li>초콜릿의 총 개수를 적을 때에는 바로 전 단계에 남아있던 초콜릿의 총 개수의 일의 자리의 값을 진법으로 하여 적는다.</li>
		<li>단, 바로 전 단계에 남아있던 초콜릿의 총 개수의 일의 자리의 값이 0 또는 1이라면, 10진법으로 적는다.</li>
	</ul>
	</li>
	<li>두 번째 줄에 남아있는 개수가 많은 순으로 각 초콜릿의 종류에 대응하는 알파벳을 공백 없이 적는다.
	<ul>
		<li>남아있는 개수가 0개인 초콜릿의 종류에 대응하는 알파벳은 적지 않는다.</li>
		<li>남아있는 개수가 동일한 초콜릿의 종류가 여러 개일 경우에는 알파벳 순으로 먼저 오는 것이 앞으로 오도록 적는다.</li>
		<li>남아있는 초콜릿의 총 개수가 0개일 경우에는 <code>NULL</code>을 적는다.</li>
	</ul>
	</li>
</ol>

<p>이제 선생님을 도와서 포스트잇에 적어야 할 초콜릿의 개수를 출력하는 코드를 작성하자!</p>

### 입력 

 <p>첫 번째 줄에 현재 종류별로 남아있는 초콜릿의 개수 $H$, $T$, $C$, $K$, $G$가 주어진다. $H$, $T$, $C$, $K$, $G$는 각각 한라봉, 감귤, 백년초, 키위, 녹차 초콜릿의 남아있는 개수이다.</p>

<p>두 번째 줄에 초콜릿을 먹는 횟수 $M$이 주어진다.</p>

<p>세 번째 줄부터 $M+2$번째 줄까지 한 번 초콜릿을 먹을 때마다 먹는 초콜릿의 개수 $h_i$, $t_i$, $c_i$, $k_i$, $g_i$가 주어진다. $h_i$, $t_i$, $c_i$, $k_i$, $g_i$는 각각 한라봉, 감귤, 백년초, 키위, 녹차 초콜릿을 먹는 개수이다.</p>

### 출력 

 <p>문제 설명에서 주어진 형식으로 총 $M \times 2$ 줄에 걸쳐 출력한다.</p>

