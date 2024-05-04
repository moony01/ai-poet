## 프로젝트 제목
AI 시 생성: [ai-poet-moony.streamlit.app](https://ai-poet-moony.streamlit.app/)

## 프로젝트 설명

Langchain framework를 활용한 AI 시 생성 앱

## 사용기술
* Langchain (OpenAI / LLama)
* Streamlit
* Python

## 개발 내용 및 이슈
- Streamlit을 사용하여 화면 구현
- Streamlit을 사용하여 Local Server 환경 구성
- Langchain을 활용하여 OpenAI(API)와 LLama(local)를 자유롭게 교체하여 실행 할 수 있도록 구현

## 설치 방법
1. 앱은 Python기반입니다. 앱을 실행하기 위해 [Python v3.9을 설치](https://www.python.org/downloads/) 합니다. (`v3.9`를 기반으로 개발하였습니다.)

2. 저장소를 clone합니다.

3. 앱에 import하고있는 library를 설치해줍니다.

```bash
pip install langchain
pip install langchain-openai
pip install streamlit
```

4. main.py를 실행할 경우 코드 맨 위 `로컬로 테스트 할 땐 아래 코드 주석을 해제해야함` 아래 코드를 주석 해제합니다.

5. 라이브러리 설치를 완료했으면 OpenAI는 `streamlit run main.py` LLama는 `streamlit run llama.py` 명령어를 실행합니다. (OpenAI는 .env 파일을 생성 후 키를 발급 받아 입력해야합니다.)

```bash
streamlit run main.py
streamlit run llama.py
```

## 로컬에서 llama 사용 방법
1. 저장소를 다운받습니다. 다운 받은 후 로직에 관련된 라이브러리를 설치하고 실행 준비를 합니다.

2. llama LLM 경량화 버전을 다운받아야 합니다. (예: llama-2-7b-chat.ggmlv3.q2_K.bin) [허깅페이스 라마 LLM 경량화 저장소 바로가기](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML)

3. llama-2-7b-chat.ggmlv3.q2_K.bin 파일인 LLM은 가장 적은 파라미터의 경량화 LLM입니다. **테스트 용도로 추천**

4. LLM을 다운 받았으면 로컬 저장소에 업로드 합니다. (llama.py와 같은 계층에)

5. LLAMA의 경우 llama.py 파일을 실행시켜줍니다.