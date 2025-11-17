
# Title: November 13, 2025 
Link: https://docs.cloud.google.com/release-notes#November_13_2025<br>
# Compute Engine
## Fixed
原文: Version `20251107.01` includes a fix for the Startup script runner component that prevented it from writing status logs and script output to Cloud Logging.
[Startup script runner](https://cloud.google.com/compute/docs/instances/startup-scripts)

説明:
Compute EngineのVMインスタンス上で動作する`Startup script runner`コンポーネントにおいて、これまでステータスログとスクリプトの出力がCloud Loggingに適切に書き込まれない問題がありましたが、バージョン`20251107.01`においてこの問題が修正されました。

影響有無:
**影響はありません。むしろ改善です。**
これは既存の機能に関するバグ修正であり、サービスの動作が安定し、ログの可視性が向上します。既存のVMインスタンスにおいて、`Startup script runner`を利用した際にCloud Loggingにログが出力されていなかった問題が解決されます。サービス停止や機能の非互換性といった負の影響はありません。

対処方法:
**特段の対処は不要です。**
この修正は、新しいVMインスタンスの作成時や、既存のVMインスタンスの基盤コンポーネントがアップデートされる際に自動的に適用されます。手動でのバージョンアップや設定変更は通常必要ありません。もし、既存のVMインスタンスで即座にこの修正を適用したい場合は、VMインスタンスの再起動または新しいVMインスタンスの作成を検討してください。

用語説明:
*   **Startup script runner**: Compute EngineのVMインスタンスが起動する際に、自動的に任意のスクリプト（シェルスクリプトやPowerShellスクリプトなど）を実行させるためのコンポーネントです。VMの初期設定、ソフトウェアのインストール、データのダウンロードなどに利用されます。
*   **Cloud Logging**: Google Cloudが提供するフルマネージドなログ管理サービスです。Google Cloudの様々なサービスやカスタムアプリケーションからログデータを収集、保存、分析し、モニタリングやトラブルシューティングに活用できます。
*   **Version `20251107.01`**: Compute EngineのVMインスタンスに適用されるエージェントや基盤イメージのバージョンを表す識別子です。Google Cloudはこれらのコンポーネントを定期的に更新し、機能改善やバグ修正を提供しています。