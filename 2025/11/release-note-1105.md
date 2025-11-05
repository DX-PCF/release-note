
# Title: November 03, 2025 
Link: https://docs.cloud.google.com/release-notes#November_03_2025<br>
# Pub/Sub
## Changed
原文:
## Libraries
## Python
## Changes for google-cloud-pubsub

[google-cloud-pubsub](https://github.com/googleapis/python-pubsub)
[2.32.0](https://github.com/googleapis/python-pubsub/compare/v2.31.1...v2.32.0)
- Adds Python 3.14 support (#1512) (95a2690)
- Debug logs (#1460) (b5d4a45)
- Support the protocol version in StreamingPullRequest (#1455) (e6294a1)

[#1512](https://github.com/googleapis/python-pubsub/issues/1512)
[95a2690](https://github.com/googleapis/python-pubsub/commit/95a26907efecfa5d56b140b7f833640b7fbb21d7)
[#1460](https://github.com/googleapis/python-pubsub/issues/1460)
[b5d4a45](https://github.com/googleapis/python-pubsub/commit/b5d4a458ca9319bebbe3142a1f05d4d4471c8d4d)
[#1455](https://github.com/googleapis/python-pubsub/issues/1455)
[e6294a1](https://github.com/googleapis/python-pubsub/commit/e6294a1883abf9809cb56d5cd4ad25cc501bc994)
- Ignore future warnings on python versions (#1546) (8e28dea)

[#1546](https://github.com/googleapis/python-pubsub/issues/1546)
[8e28dea](https://github.com/googleapis/python-pubsub/commit/8e28dea5b68fc940266d0b1a9f2a07a7b5f10b34)

説明：
Google Cloud Pub/Sub の Python クライアントライブラリ `google-cloud-pubsub` がバージョン 2.32.0 に更新されました。このバージョンには以下の変更が含まれています。
*   **Python 3.14 のサポート追加**: 最新の Python バージョンである 3.14 への対応が追加されました。
*   **デバッグログの強化**: クライアントライブラリからのデバッグ出力が改善され、より詳細な情報が得られるようになりました。
*   **StreamingPullRequest におけるプロトコルバージョンサポート**: Pub/Sub の StreamingPull API における内部プロトコルバージョン指定のサポートが追加され、クライアントが最新のプロトコル機能を利用できるようになりました。
*   **将来の Python バージョンでの警告無視**: 将来の Python バージョンで発生する可能性のある `FutureWarning` を無視するロジックが追加されました。

影響有無：
**影響なし**。
理由：
Google Cloud Composer 2 (Composer version 2.7.1, Airflow version 2.7.3) 環境は現在 Python 3.9 をベースとしており、今回追加された Python 3.14 のサポートは直接的な影響を与えません。本リリースは、既存機能に対する破壊的変更（Breaking Change）を含まず、機能の追加、内部的な改善、デバッグ機能の強化が主であるため、既存の Airflow DAGs や Pub/Sub との連携ロジックに悪影響を及ぼす可能性は極めて低いと判断されます。Google Cloud Composer 環境は Google によって管理されており、プリインストールされているクライアントライブラリのバージョンは、Google側で互換性が検証された上で Composer の新しい環境イメージとして提供されるため、現行の運用中の環境には即座に影響はありません。

対処方法：
なし。
本変更は機能追加および改善であり、既存の Google Cloud Composer 環境の動作に影響を与えるものではないため、特別な対応は不要です。将来的に Airflow 環境の Python バージョンをアップグレードする場合や、`google-cloud-pubsub` ライブラリのバージョンを明示的に更新する場合に、これらの改善の恩恵を受けることができます。

用語説明：
*   **google-cloud-pubsub**: Google Cloud Pub/Sub サービスとのプログラム的な連携を可能にするための Python 用のクライアントライブラリです。メッセージの発行や購読を行う際に利用されます。
*   **Google Cloud Composer**: Google Cloud 上で Apache Airflow を実行・管理するためのフルマネージドサービスです。データパイプラインやバッチ処理のワークフローオーケストレーションに利用されます。
*   **Apache Airflow**: プログラマブルにデータパイプラインやワークフローを定義、スケジュール、監視できるオープンソースのプラットフォームです。
*   **StreamingPullRequest**: Google Cloud Pub/Sub のサブスクリプションからメッセージを受信する際の効率的なメカニズムの一つです。クライアントがサービスとの間でストリーミング接続を確立し、継続的にメッセージを受信することを可能にします。
*   **FutureWarning**: Python における警告カテゴリの一つで、将来のバージョンで変更される可能性のある動作や非推奨となる機能を使用している場合に発生します。通常、プログラムの実行を中断させることはありませんが、将来的な互換性の問題を示唆します。