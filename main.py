from fastapi import FastAPI
from api.users import router as user_router
from api.courses import router as course_router
from api.sections import router as section_router

app = FastAPI(
    title="FastAPI LMS",
    description="lms for managing students and courses",
    version="0.0.1",
    contact={
        "name": "Fabian Landeros",
        "email": "landerosedgard@gmail.com"
    },
    license_info={
        "name": "MIT",
        "url": "https://opensource.org/licenses/MIT"
    },

)

app.include_router(router=user_router)
app.include_router(router=course_router)
app.include_router(router=section_router)

#min59
