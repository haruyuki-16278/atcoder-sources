import sequtils
import strutils
import strformat

let A = stdin.readLine.parseInt # 500円玉
let B = stdin.readLine.parseInt # 100円玉
let C = stdin.readLine.parseInt #  50円玉
let X = stdin.readLine.parseInt # 目標金額

var ways: int = 0
for i in countup(0, A):
    for j in countup(0, B):
        for k in countup(0, C):
            let s = i * 500 + j * 100 + k * 50
            if s == X:
                inc ways

echo ways
