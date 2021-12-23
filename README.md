# Capstone Project
#### By Matthew Laude

## Dependencies
- cors
- dotenv
- gunicorn
- psycopg2

## Models
Ice:
- name: string
- image: string
- caption: string
- description: string
- ingredients: string

## Backend Route Table 
| url | method | action |
|-----|--------|--------|
| /ice | get | getting all the ice creams (index)||
| /ice | post | posting a new ice cream (create) |
| /ice/:id | put | updating an ice cream (update) |
| /ice/:id | delete | deleting an ice cream (destroy) |
