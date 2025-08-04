#include <gtest/gtest.h>
#include "queue.h"

class QueueTest : public ::testing::Test {
protected:
    void SetUp() override {
        q.push(10);
        q.push(20);
    }

    Queue<int> q;
};

TEST_F(QueueTest, IsEmptyInitially) {
    Queue<int> emptyQ;
    EXPECT_TRUE(emptyQ.empty());
}

TEST_F(QueueTest, PushIncreasesSize) {
    EXPECT_EQ(q.size(), 2);
    q.push(30);
    EXPECT_EQ(q.size(), 3);
}

TEST_F(QueueTest, PopReturnsFrontElement) {
    EXPECT_EQ(q.pop(), 10);
    EXPECT_EQ(q.pop(), 20);
}

TEST_F(QueueTest, PopDecreasesSize) {
    q.pop();
    EXPECT_EQ(q.size(), 1);
}