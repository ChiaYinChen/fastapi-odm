db = db.getSiblingDB('dev');
db.createUser(
    {
        user: "devUser",
        pwd: "devUser",
        roles: [{ role: "readWrite", db: "dev" }]
    }
);
db.createCollection('test');
print("Initialization script has been executed");