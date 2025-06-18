# # import asyncio

# # async def fetch_data():
# #     print ("Start fetching ...")
# #     await asyncio.sleep(2)  # simulate IO delay

# #     print ("Done!")
# #     return {"data": 123}

# # async def main():
# #     result = await fetch_data()
# #     print(result)


# # asyncio.run(main())

# # '''
# # 1. Run main() via asyncio.run()
# # 2. main() calls fetch_data() using await
# # 3. fetch_data() prints "Start fetching ..."
# # 4. Pauses for 2 seconds (non-blocking)
# # 5. Resumes → prints "Done!"
# # 6. Returns data → main() prints the result

# # '''
# ## 🐢 1. Synchronous Version (Normal Blocking)
# # import time
# # def brush_teeth():
# #     print("Brushing teeth...")
# #     time.sleep(5)
# #     print ("Done Brushing!")

# # def toast_bread():
# #     print("Toasting bread...")
# #     time.sleep(2)  # Takes 2 seconds
# #     print("Done toasting!")

# # def main():
# #     brush_teeth()
# #     toast_bread()

# # main()

# ###⚡ 2. Asynchronous Version (Efficient, Non-blocking)

# import asyncio

# async def brush_teeth():
#     print("Brushing teeth...")
#     await asyncio.sleep(3)  # Non-blocking 3s delay
#     print("Done brushing!")

# async def toast_bread():
#     print("Toasting bread...")
#     await asyncio.sleep(2)  # Non-blocking 2s delay
#     print("Done toasting!")

# async def main():
#     # Run both tasks at the same time
#     await asyncio.gather(
#         brush_teeth(),
#         toast_bread()
#     )

# asyncio.run(main())


from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Define the request body schema
class User(BaseModel):
    name: str
    email: str
    age: int

# Define a POST endpoint that receives the request body
@app.post("/create_user/")
async def create_user(user: User):
    return {
        "message": "User created successfully!",
        "user_data": user
    }
