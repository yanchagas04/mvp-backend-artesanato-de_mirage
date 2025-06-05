/*
  Warnings:

  - You are about to drop the column `artesao_id` on the `Produto` table. All the data in the column will be lost.

*/
-- CreateTable
CREATE TABLE "_artesao_id" (
    "A" INTEGER NOT NULL,
    "B" INTEGER NOT NULL,
    CONSTRAINT "_artesao_id_A_fkey" FOREIGN KEY ("A") REFERENCES "Artesao" ("id") ON DELETE CASCADE ON UPDATE CASCADE,
    CONSTRAINT "_artesao_id_B_fkey" FOREIGN KEY ("B") REFERENCES "Produto" ("id") ON DELETE CASCADE ON UPDATE CASCADE
);

-- RedefineTables
PRAGMA defer_foreign_keys=ON;
PRAGMA foreign_keys=OFF;
CREATE TABLE "new_Produto" (
    "id" INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "nome" TEXT NOT NULL,
    "descricao" TEXT NOT NULL,
    "preco" REAL NOT NULL,
    "data_cadastro" DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);
INSERT INTO "new_Produto" ("data_cadastro", "descricao", "id", "nome", "preco") SELECT "data_cadastro", "descricao", "id", "nome", "preco" FROM "Produto";
DROP TABLE "Produto";
ALTER TABLE "new_Produto" RENAME TO "Produto";
PRAGMA foreign_keys=ON;
PRAGMA defer_foreign_keys=OFF;

-- CreateIndex
CREATE UNIQUE INDEX "_artesao_id_AB_unique" ON "_artesao_id"("A", "B");

-- CreateIndex
CREATE INDEX "_artesao_id_B_index" ON "_artesao_id"("B");
