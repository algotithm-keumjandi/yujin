import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while(len(scoville) > 1):
        min_score = heapq.heappop(scoville)
        if min_score >= K:
            break
        heapq.heappush(scoville, min_score + heapq.heappop(scoville) * 2)
        # heapq.heapify(scoville) -> 힙 속성을 유지하면서 동작하므로 별도로 호출할 필요 X
        answer += 1
    
    if scoville[0] < K:
        answer = -1
    
    return answer
