from fastapi import APIRouter
from fastapi import Request, Response, HTTPException
from fastapi.params import Body
from pydantic import BaseModel, Field,constr,confloat
from typing import List, Optional, Literal


class GigCreate(BaseModel):
    id: int = Field(..., description="Auto incremented ID of the gig item")
    title: str = Field(..., min_length=5, max_length=100)
    description: str = Field(..., min_length=20, max_length=500)
    category: Literal["Development", "Design", "Writing"]
    currency: Literal["USD"] = Field(..., description="Currency of the budget")
    client_name: str = Field(...,min_length=2,max_length=50)

class GigUpdate(BaseModel):
    budget: float = Field(..., gt=0)
    status: Literal["Open", "In Progress", "Closed"] = Field(...,description="Current status of the gig item")

gigs_dt = [
    {"id" : 1, "title" : "Build a react dashboard", "description" : "Build a React dashboard for a fintech startup. Must be responsive and mobile-friendly.", "category" : "Development", "budget" : 15000.0, "currency" : "USD", "status" : "Open", "client_name" : "Jane Mutoni"}, #1
    {"id" : 2, "title" : "Design a logo for a tech company", "description" : "Create a modern logo for a tech company. The logo should be simple and memorable.", "category" : "Design", "budget" : 500.0, "currency" : "USD", "status" : "Open", "client_name" : "Wendy Johnson"}, #2
    {"id" : 3, "title" : "Write technical documentation", "description" : "Write comprehensive technical documentation for a software product.", "category" : "Writing", "budget" : 2000.0, "currency" : "USD", "status" : "Open", "client_name" : "Alice Smith"}, #3
    {"id" : 4, "title" : "Develop a mobile app", "description" : "Develop a cross-platform mobile app for iOS and Android.", "category" : "Development", "budget" : 25000.0, "currency" : "USD", "status" : "Open", "client_name" : "Bob Johnson"}, #4
    {"id": 5, "title" : "Create a marketing plan", "description" : "Develop a comprehensive marketing plan for a new product launch.", "category" : "Writing", "budget" : 3000.0, "currency" : "USD", "status" : "Open", "client_name" : "Carol Williams"}, #5
    {"id": 6, "title" : "Conduct user research", "description" : "Perform user research to gather insights for product development.", "category" : "Development", "budget" : 1000.0, "currency" : "USD", "status" : "Open", "client_name" : "David Brown"}, #6
    {"id": 7, 'title': 'Design a website layout', 'description': 'Create a modern website layout for a e-commerce business.', 'category': 'Design', 'budget': 1500.0, 'currency': 'USD', 'status': 'Open', 'client_name': 'Eve Davis'}, #7
    {"id": 8, 'title': 'Write blog posts', 'description': 'Write engaging blog posts for a tech blog.', 'category': 'Writing', 'budget': 1000.0, 'currency': 'USD', 'status': 'Open', 'client_name': 'Frank Wilson'}, #8
    {"id" : 9, "title" : "Create social media content", "description" : "Develop creative social media content for a fashion brand.", "category" : "Design", "budget" : 2000.0, "currency" : "USD", "status" : "Open", "client_name" : "Grace Lee"}, #9
    {"id" : 10, "title" : "Develop a landing page", "description" : "Create an attractive landing page for a SaaS product.", "category" : "Development", "budget" : 1500.0, "currency" : "USD", "status" : "Open", "client_name" : "Henry Taylor"}, #10
    {"id": 11, "title" : "Optimize website performance", "description" : "Improve the loading speed and overall performance of a website.", "category" : "Development", "budget" : 2000.0, "currency" : "USD", "status" : "Open", "client_name" : "Ivy Chen"}, #11
    {"id": 12, "title" : "Design a mobile app UI", "description" : "Create a user-friendly and visually appealing UI for a mobile app.", "category" : "Design", "budget" : 3000.0, "currency" : "USD", "status" : "Open", "client_name" : "Jackie Kim"} #12
]

router = APIRouter()

#Returns the list of gigs available in the system. 
@router.get("/gigs")
def get_list():
    return {"gigs": gigs_dt}


#Search for gigs based on a query string
@router.get("/gigs/search")
def search_gigs(q: str):
    results = []
    for gig in gigs_dt:
        if q.lower() in gig["title"].lower() or q.lower() in gig["description"].lower():
            results.append(gig)
    return {"results": results}

#Search for gigs based on a query string and category
@router.get("/gigs/{gig_id}")
def get_gig(gig_id: int):
    for gig in gigs_dt:
        if gig["id"] == gig_id:
            return {"gig" : gig}
    raise HTTPException(status_code=404, detail="Gig not found")

#Create a new gig item
@router.post("/gigs/create")
def create_gig(gig_item: GigCreate = Body(...)):
    new_id = max(gig["id"] for gig in gigs_dt) + 1
    gig_item.id = new_id
    gigs_dt.append(gig_item.model_dump())
    return {"message" : "Gig posted successfully", "gig" : gig_item.model_dump()}

#Update an existing gig item
@router.put("/gigs/update/{gig_id}")
def update_gig(gig_id: int, gig_item: GigUpdate = Body(...)):
    for i, gig in enumerate(gigs_dt):
        if gig["id"] == gig_id:
            gigs_dt[i].update(gig_item.model_dump()) #>
            return {
                "message": "Gig updated successfully",
                "gig": gigs_dt[i]
            }
    raise HTTPException(status_code=404, detail="Gig not found")


#Delete a gig item
@router.delete("/gigs/delete/{gig_id}")
def delete_gig(gig_id: int):
    for i, gig in enumerate(gigs_dt):
        if gig["id"] == gig_id:
            gigs_dt.pop(i)
            return {"message" : "Gig deleted successfully"}
    raise HTTPException(status_code=404, detail="Gig not found")