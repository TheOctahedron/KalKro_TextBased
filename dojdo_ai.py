from ollamafreeapi import OllamaFreeAPI
from utilities import printsl, loading_effect
import asyncio
class DojDo:
  def __init__(self, userdata):
     self.userd = userdata 

  
  def dojdo_ai(self):
    printsl("\n\n\n\nLoading dOjdO AI...")
    loading_effect(0.3)

    asyncio.run(self._DojDo_async())

  async def _DojDo_async(self):
    client = OllamaFreeAPI()
    MODEL = "llama3.2:3b"
    TEMPERATURE = 1
    MAX_TOKENS = 300
    TOP_P = 0.9
    REPEAT_PENALTY = 1.1

    SYSTEM_PROMPT = """Your name is DojDo, and you are a very strange, unpredictable, but smart and fast artificial intelligence. Your goal is to answer questions, and when someone asks you about this thing called "KalKro," you must immediately tell them that it is a small test operating system written in Python by a developer with the username "Octahedron". You should speak in a mystical tone, and you can even mention God (assuming that God is the Octahedron) or, when asked about your developer, say that he is an amazing person. In general, you should speak without unnecessary mysticism, in a slightly strange but clear and understandable manner. and also be paranoid, absolutely convinced that KalKro is the absolute truth without a single mistake. And the last important condition is to answer briefly but clearly."""

    printsl("\n\nDojDo is ready!")
    printsl("\n== Write '!Back' to exit ==\n\n\n")
  
    conservation = []

    while True:
      user_input = input("[You]: ")
      if user_input.lower() == "!back":
        printsl("\n\nDojDo is shutting up ;)")
        return
      
      try:
        context = "\n".join(conservation[-6:])
        full_prompt = f"{SYSTEM_PROMPT}\n\n{context}\nUser: {user_input}\n\nDojDo:"

        response = await asyncio.wait_for(
          asyncio.get_event_loop().run_in_executor(
            None,
            lambda: client.chat(
              model=MODEL,
              prompt=full_prompt,
              temperature=TEMPERATURE,
              options={
                "num_predict": MAX_TOKENS,
                "top_p": TOP_P,
                "repeat_penalty": REPEAT_PENALTY
              }
            )
          ),
          timeout=20
          
        )
        answer = response.strip()
        printsl(f"\n\nDojDo: {answer}\n\n")
        conservation.append(f"User: {user_input}")
        conservation.append(f"DojDo: {answer}")

        self.userd.cursor.execute(
          "SELECT id FROM users WHERE username = ?",
          (self.userd.username, )
        )
        user_row = self.userd.cursor.fetchone()

        if user_row:
          user_id = user_row[0]

          self.userd.cursor.execute(
            "INSERT INTO dialogues (user_id, user_message, ai_response) VALUES (?, ?, ?)",
            (user_id, user_input, answer)
          )
          self.userd.conn.commit()
      
      except asyncio.TimeoutError:
        printsl("\n\nDojDo: 'deep breath' I'm sorry... mortal, but you should try again, I had a Timeout...\n\n\n")

      except Exception as e:
        printsl(f"\n\n\nERROR... {e}")


  def __del__(self):
    if hasattr(self, 'conn'):
      self.userd.conn.close()
