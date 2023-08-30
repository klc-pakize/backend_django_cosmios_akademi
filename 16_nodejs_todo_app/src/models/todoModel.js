const { Pool } = require("pg");

const pool = new Pool({
  user: "postgres",
  host: "localhost",
  database: "databaseverdiğinizisim",
  password: "kendişifreniz",
  port: 5432,
});

const createTodoTable = async () => {
  try {
    const creatTableQuery = `
            CREATE TABLE IF NOT EXISTS todo(
                id SERIAL PRIMARY KEY,
                name VARCHAR NOT NULL,
                description TEXT NOT NULL,
                completed BOOLEAN DEFAULT FALSE,
                created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP, 
                updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
            )
        `;

    const client = await pool.connect();
    await client.query(creatTableQuery);
    client.release();
    console.log("Tobla başarıyla oluşturuldu");
  } catch (error) {
    console.log("Tablo oluşturulamadı", error);
  }
};

module.exports = { pool, createTodoTable };
