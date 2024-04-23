## URL:
https://ai-poet-moony.streamlit.app/

## 사용기술
* Langchain Open AI / LLama
* Streamlit
* Python

## 로컬에서 llama 사용 방법
1. 저장소를 다운받습니다. 다운 받은 후 로직에 관련된 라이브러리를 설치하고 실행 준비를 합니다.

2. llama LLM 경량화 버전을 다운받아야 합니다. (예: llama-2-7b-chat.ggmlv3.q2_K.bin) [허깅페이스 라마 LLM 경량화 저장소 바로가기](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML)

3. llama-2-7b-chat.ggmlv3.q2_K.bin 파일인 LLM은 가장 적은 파라미터의 경량화 LLM입니다. **테스트 용도로 추천**

5. LLAMA의 경우 llama.py 파일을 실행시켜줍니다. (open ai는 .env에 키를 발급 받아 입력해야합니다.)

## 로컬 스트림릿 서버 실행
```bash
streamlit run main.py
```

## git 명령어

### commit으로 인해 stage에 올라간 commit 취소
```bash
git reset HEAD~1            // 커밋 취소하고 변경사항을 스테이지에서 내리기(단순버전)

or

git reset --mixed HEAD~1    // 커밋 취소하고 변경사항을 스테이지에서 내리기

or

git reset --soft HEAD~1     // 최근 커밋 취소하기
```