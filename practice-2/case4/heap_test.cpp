#include <gtest/gtest.h>
#include "heap.h"

class HeapTest : public ::testing::Test {
protected:
    void SetUp() override {
        h.push(30);
        h.push(10);
        h.push(50);
    }

    Heap<int> h;
};

TEST_F(HeapTest, TopReturnsMaxElement) {
    EXPECT_EQ(h.top(), 50);
}

TEST_F(HeapTest, PushMaintainsHeapProperty) {
    h.push(60);
    EXPECT_EQ(h.top(), 60);
}

TEST_F(HeapTest, PopRemovesTopElement) {
    h.pop();
    EXPECT_EQ(h.top(), 30);
}

TEST_F(HeapTest, HeapifyWorks) {
    Heap<int> h2 = {5, 15, 1};
    EXPECT_EQ(h2.top(), 15);
}