# 파일이름 :
# 작 성 자 :
# 1. 비어있는 리스트 bucket_list 만들기
bucket_list = []

# 2. input()을 3번 사용하여 맛집 3곳 입력받고 리스트 맨 뒤에 추가(append)
place1 = input("맛집 리스트 입력: ")
bucket_list.append(place1)

place2 = input("맛집 리스트 입력: ")
bucket_list.append(place2)

place3 = input("맛집 리스트 입력: ")
bucket_list.append(place3)

# 첫 번째 미션 후 리스트 출력 (화면 예시 참고)
print(f"리스트: {bucket_list}\n")

# 3. '1순위 VIP 맛집'을 입력받고 리스트의 맨 앞(0번 인덱스)에 삽입(insert)
vip_place = input("맛집 리스트 추가: ")
bucket_list.insert(0, vip_place)

# 두 번째 미션 후 리스트 출력
print(f"리스트 : {bucket_list}\n")

# 4. '오늘 방문한 맛집'을 입력받고 리스트에서 삭제(remove)
visited_place = input("도장 깨기: ")
bucket_list.remove(visited_place)

# 5. 최종 bucket_list 출력
print(f"리스트 : {bucket_list}")