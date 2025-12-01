.PHONY: help build up down logs test test-verbose clean

help:
	@echo "利用可能なコマンド:"
	@echo "  make build          - Dockerイメージをビルド"
	@echo "  make up             - Dockerコンテナを起動"
	@echo "  make down           - Dockerコンテナを停止"
	@echo "  make logs           - Dockerコンテナのログを表示"
	@echo "  make test           - テストを実行"
	@echo "  make test-verbose   - 詳細なテスト出力"
	@echo "  make clean          - Dockerコンテナとイメージをクリーンアップ"

build:
	docker-compose build

up:
	docker-compose up -d

down:
	docker-compose down

logs:
	docker-compose logs -f

test:
	docker-compose exec fastapi-app pytest test_main.py

# 詳細なテスト出力
test-verbose:
	docker-compose exec fastapi-app pytest test_main.py -v

clean:
	docker-compose down --rmi all
