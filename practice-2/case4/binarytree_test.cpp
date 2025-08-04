#include <gtest/gtest.h>
#include "binarytree.h"

class BinaryTreeTest : public ::testing::Test {
protected:
    void SetUp() override {
        tree.insert(50);
        tree.insert(30);
        tree.insert(70);
    }

    BinaryTree<int> tree;
};

TEST_F(BinaryTreeTest, SearchFindsExistingElement) {
    EXPECT_TRUE(tree.search(30));
    EXPECT_FALSE(tree.search(99));
}

TEST_F(BinaryTreeTest, InsertAddsElements) {
    tree.insert(25);
    EXPECT_TRUE(tree.search(25));
}

TEST_F(BinaryTreeTest, PopRemovesElement) {
    tree.pop(30);
    EXPECT_FALSE(tree.search(30));
}

TEST_F(BinaryTreeTest, InOrderTraversal) {
    std::vector<int> expected = {30, 50, 70};
    EXPECT_EQ(tree.inorder(), expected);
}