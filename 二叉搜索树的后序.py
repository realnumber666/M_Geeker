# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, seq):
        # write code here
        if len(seq) == 0:
            return False

        if len(seq) <= 2:
            return True

        for i in range(len(seq)):
            if seq[i] > seq[-1]:
                break

        for n in seq[i:-1]:
            if n < seq[-1]:
                return False

        # 如果长度已经为零需要提前拦截，len(seq) == 0只是为了把输入即为空的情况给排除掉
        boolRight = self.VerifySquenceOfBST(seq[:i]) if len(seq[:i]) != 0 else True
        boolLeft = self.VerifySquenceOfBST(seq[i:-1]) if len(seq[i:-1]) != 0 else True
        return boolRight and boolLeft