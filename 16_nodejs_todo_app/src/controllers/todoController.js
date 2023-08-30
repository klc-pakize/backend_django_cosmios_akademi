const { pool } = require("../models/todoModel");

const todoAdd = async (req, res) => {
  try {
    const { name, description, completed } = req.body;

    const insertValues = [name, description, completed];

    const insertQuery = `
        INSERT INTO todo(name, description, completed, created_at, updated_at) VALUES ($1, $2, $3, CURRENT_TIMESTAMP,CURRENT_TIMESTAMP) RETURNING*;
    `;

    const client = await pool.connect();
    const insertResault = await client.query(insertQuery, insertValues);
    const todoAdded = insertResault.rows[0];
    client.release();
    return res.status(201).json(todoAdded);
  } catch (error) {
    console.error("Kayıt oluşturulmadı..", error);
    return res.status(500).json({
      success: false,
      message: "Kayıt oluşturulmadı..",
    });
  }
};

const todoGetAll = async (req, res) => {
  try {
    const query = `SELECT * FROM todo`;

    const client = await pool.connect();
    const insertResault = await client.query(query);
    const todos = insertResault.rows;
    client.release();
    return res.status(200).json(todos);
  } catch (error) {
    console.error("Kayıt bulunmadı..", error);
    return res.status(500).json({
      success: false,
      message: "Kayıt bulunamadı..",
    });
  }
};

const todoUpdate = async (req, res) => {
  try {
    const { id, name, description, completed } = req.body;

    const updatedQuery = `
            UPDATE todo
            SET name = $1, description = $2, completed = $3 , updated_at = CURRENT_TIMESTAMP
            WHERE id = $4
             RETURNING*;
        `;

    const values = [name, description, completed, id];
    const client = await pool.connect();
    const resault = await client.query(updatedQuery, values);
    const updatedTodo = resault.rows;
    client.release();
    return res.status(201).json(updatedTodo);
  } catch (error) {
    console.error("Kayıt güncellenmedi..", error);
    return res.status(500).json({
      success: false,
      message: "Kayıt güncellenmedi..",
    });
  }
};

const todoDelete = async (req, res) => {
  try {
    const id = req.params.id;

    const deleteQuery = `
        DELETE FROM todo
        WHERE id = $1
        RETURNING*;
        `;

    const value = [id];

    const client = await pool.connect();
    const resault = await client.query(deleteQuery, value);
    client.release();
    const deletedTodo = resault.rows[0];

    if (!deletedTodo) {
      return res.status(404).json({
        success: false,
        message: "Kayıt bulunamadı..",
      });
    }

    return res.status(200).json(deletedTodo);
  } catch (error) {
    console.error("Kayıt silinirken hata oluştu..", error);
    return res.status(500).json({
      success: false,
      message: "Kayıt silinirken hata oluştu..",
    });
  }
};

const todoGet = async (req, res) => {
  try {
    const id = req.params.id;

    const getQuery = `
      SELECT * FROM todo
      WHERE id = $1;
    `;

    const values = [id];

    const client = await pool.connect();
    const result = await client.query(getQuery, values);
    client.release();

    const todo = result.rows[0];

    if (!todo) {
      return res.status(404).json({
        success: false,
        message: "Kayıt bulunamadı..",
      });
    }

    return res.status(200).json(todo);
  } catch (error) {
    console.error("Kayıt alınırken hata oluştu..", error);
    return res.status(500).json({
      success: false,
      message: "Kayıt alınırken hata oluştu..",
    });
  }
};

module.exports = { todoAdd, todoGetAll, todoUpdate, todoDelete, todoGet };
