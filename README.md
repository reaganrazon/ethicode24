## EthiCode

With new developments in AI and growing considerations about both how we will introduce education technology to the classroom, and how we will refine computer science education, it begs the question of how to design with students in mind. As a computer science major who is studying child policy research, I care immensely about working towards equity in education, and more specifically computer science education.

Having worked in various public school systems, as a mentor and volunteer, as an intern at an educational technology startup, and as a fellow developing curricula with public school teachers, I have interacted with many important parties: students, teachers, parents, families, and board members. When it comes to computer science curriculum and development, there can be a disconnect between policy and practice. It is easy to throw some tools at a teacher, or some frameworks. The hard part is understanding what teachers and students need, and how we can also make the "black box" of algorithms and computing more transparent.

At Duke, I am learning about and focusing on "Open-Design" which is "an equity-focused innovation methodology that foregrounds active inclusivity, transparency, and collaboration." When applied to curriculum development and lesson planning, this means that "open design enables students and teachers to develop critical, creative, and courageous thinking skills and habits of mind necessary for a participatory and self-determined life."

# What it does
This web application, EthiCode, serves as a way to support and guide teachers in learning about Open-Design and integrating ethical considerations into computer science curriculum development. The first page discusses the guiding values of open-design. Underneath, to emulate the understand phase, there is a chatbot where teachers can send in inquiries they have about ethics, equity, gender and computing, open-design, and more. The second page, the create page, is where educators can upload both their favorite lesson plan and their county standards. This information goes into a secure database. Then, the output would be lesson plan ideas for the teachers that keep in mind the county standards, previous lessons that their students liked, all while aligning with an ethics-centered framework.

# How we built it
I used Reflex to create the frontend and backend of my app, all based in python. I used InterSystems IRIS for the database, which allowed me to use embedding models, translate my text to vectors, store these vectors in IRIS, and then query text. To gather the text, I used a pdf parsing function in python to translate academic articles to text files. At a high level, the flow is User query → relevant data → feed it to the LLM as context. Following recommendations from InterSystems, I used LLAMA index to develop this Retrieval-Augmented Generation (RAG) system. I also did some fine-tuning to calibrate some of the responses.

# Challenges we ran into
It was very difficult connecting the front and backend, figuring out what models to use, actually being able to run things without using all my RAM, and synthesizing my idea. Picking up a new framework was also difficult but incredibly rewarding.

