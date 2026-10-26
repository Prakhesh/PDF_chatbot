# 1.  Database ko import kiya (Loader, chunking sab ek baar chal jayega)
from utils.embeddings import vectorstore

print("\n--- Fast PDF Chatbot Active ---")

# 2. Infinite Loop chalaya taaki har sawal instant (1 second me) chale
while True:
    # User se English me sawal poochna
    query = input("\nAsk your question (or type 'exit' to quit): ")
    
    # Agar user 'exit' likhe, toh program band kar do
    if query.lower() == 'exit':
        print("Chatbot stopped.")
        break
        
    # 3. Database se score ke sath sabse best matching answer (k=1) dhoodhna
    results = vectorstore.similarity_search_with_score(query, k=1)
    
    # 4. Loop chala kar check karna ki answer kaam ka hai ya nahi
    for doc, score in results:
        # Agar score 0.6 se bada hai, matlab sawal PDF me nahi hai
        if score > 1.1:
            print("❌ Answer not found in the PDF.")
        else:
            print("🤖 ANSWER:")
            print(doc.page_content)