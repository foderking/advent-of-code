import nimpy
import std/[md5, strutils, sequtils, sugar]


proc greet(name: string): string {.exportpy.} =
  return "Hello, " & name & "!"

proc partOne*(input: string): string {.exportpy}=
  var
    i = 0
    tmp: string
    hash: string

  while result.len<8:
    tmp = input&($i)
    hash = $tmp.toMD5

    #echo("hashing", tmp)

    if "00000" == hash[0..<5]:
      result &= hash[5]
      echo(tmp,": ", hash)
    i+=1

proc partTwo*(input: string): string {.exportpy}=
  var
    ans= newSeq[string](8)
    set= newSeq[bool](8)
    tmp: string
    hash: string
    ind: string
    i = 0

  while not all(set, (each) => each):
    tmp = input&($i)
    hash = $tmp.toMD5
    ind  = ($hash[5])
  
    if "00000"==hash[0..<5] and ind<"8" and not set[ind.parseInt]:
      echo(tmp,": ", hash, " ", ind)
      ans[ind.parseInt] = $hash[6]
      set[ind.parseInt] = true
    i+=1
  return ans.join("")
