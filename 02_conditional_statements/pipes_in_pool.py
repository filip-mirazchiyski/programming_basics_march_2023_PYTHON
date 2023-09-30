V = int(input())
P1 = int(input())
P2 = int(input())
N = float(input())

pipe_1 = P1 * N
pipe_2 = P2 * N
total_pipe = pipe_1 + pipe_2
total_pipe_percentage = total_pipe / V * 100
pipe_1_percentage = (pipe_1 / total_pipe * 100)
pipe_2_percentage = (pipe_2 / total_pipe * 100)
#print(f"{total_pipe_percentage:.0f}")
diff = total_pipe - V

if total_pipe <= V:
    print(f"The pool is {total_pipe_percentage:.2f}% full. Pipe 1: {pipe_1_percentage:.2f}%. \
Pipe 2: {pipe_2_percentage:.2f}%")
else:
    print(f"For {N:.2f} hours the pool overflows with {diff:.2f} liters.")
