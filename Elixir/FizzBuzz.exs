#!/usr/bin/elixir

defmodule FizzBuzz do
	def getNumber(n) do
		run(1, n)
	end

	defp run(x, n) when x == n do
		cond do
			rem(x, 15) == 0 -> IO.puts "#{x}: FizzBuzz"
			rem(x, 5) == 0 -> IO.puts "#{x}: Fizz"
			rem(x, 3) == 0 -> IO.puts "#{x}: Buzz"
			true	-> nil
		end
	end
	defp run(x, n) do
		run(x, x)
		run(x + 1, n)
	end
end


input = 30
FizzBuzz.getNumber(input);

