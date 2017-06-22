n = gets.chomp.to_i

def pascal(n)
  result = [[1],[1,1]]
  if n == 2
    return result
  else
    result = pascal(n-1)
    result << (0..n-1).to_a
    result[-1][0] = 1
    for x in 1..n-2
      result[n-1][x] = result[n-2][x-1] + result[n-2][x]
    end
    result[-1][-1] = 1
    return result
  end
end


print pascal(n)
