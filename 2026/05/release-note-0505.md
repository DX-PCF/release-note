
# Title: May 01, 2026 
Link: https://docs.cloud.google.com/release-notes#May_01_2026<br>
# Google Kubernetes Engine

## Announcement

**原文:**
Kubernetes 1.36 is now available in the Rapid channel. For more information about the content of Kubernetes 1.36, see Kubernetes 1.36 release notes, and Kubernetes 1.36 Release Blog.

[Kubernetes 1.36 release notes](https://github.com/kubernetes/kubernetes/blob/master/CHANGELOG/CHANGELOG-1.36.md#changelog-since-v1350)
[Kubernetes 1.36 Release Blog](https://kubernetes.io/blog/2026/04/22/kubernetes-v1-36-release/)

**説明:**
GKEのリリースチャネルの一つであるRapidチャネルで、Kubernetesバージョン1.36が利用可能になったことがアナウンスされました。Kubernetes 1.36に関する具体的な変更点や新機能、非推奨化されたAPIなどの詳細は、提供されたKubernetesの公式リリースノートおよびリリースブログを参照してください。Rapidチャネルは、最新のKubernetesバージョンを早期に利用できるため、開発やテスト、新機能の先行評価などに適しています。

**影響有無:**
既存のGKEクラスタへの直接的な影響は現時点ではありません。
*   **影響なし**: 貴社のGKEクラスタがRapidチャネルを使用しておらず、かつKubernetes 1.36への自動アップグレードが有効になっていない場合、または手動アップグレードを実施しない限り、現在の運用に影響はありません。
*   **影響ありの可能性**:
    *   貴社のGKEクラスタが**Rapidチャネル**を使用しており、自動アップグレードが有効になっている場合、Kubernetes 1.36への自動アップグレードの対象となる可能性があります。この場合、Kubernetes 1.36に含まれるAPI変更、機能変更、非推奨化などが既存のワークロードに影響を与える可能性があります。
    *   将来的に、Stableチャネルなど他のリリースチャネルにもKubernetes 1.36が提供されると、すべてのGKEユーザーがこのバージョンへのアップグレードを検討する必要が出てきます。

**対処方法:**
1.  **GKEクラスタのリリースチャネルの確認**:
    *   現在運用中のGKEクラスタがどのリリースチャネルに属しているかを確認してください。
    *   もしRapidチャネルを使用している場合は、Kubernetes 1.36へのアップグレード計画を検討する必要があります。
2.  **Kubernetes 1.36のリリースノートの確認**:
    *   提供されたリンク（Kubernetes 1.36 release notes, Kubernetes 1.36 Release Blog）を参照し、Kubernetes 1.36の主要な変更点、特に「Breaking Changes（破壊的変更）」や「Deprecations（非推奨化）」を確認してください。
    *   アプリケーションやKubernetesマニフェストがこれらの変更に影響を受ける可能性があるかを評価してください。
3.  **テスト環境での検証 (Rapidチャネル利用者向け)**:
    *   Rapidチャネルを使用している場合、本番環境への適用前に、テスト環境でKubernetes 1.36へのアップグレードをシミュレートし、既存のワークロードが問題なく動作するかを十分に検証することを推奨します。

**用語説明:**
*   **Rapid channel (GKE)**: Google Kubernetes Engineのリリースチャネルの一つ。最新のKubernetesバージョンが最も早く提供されるチャネルであり、新機能を早期に利用できる反面、他のチャネルに比べてサポート期間が短く、マイナーバージョンのリリース間隔も短いため、開発・テスト環境や最新技術の検証に用いられることが多いです。
*   **Kubernetes 1.36**: コンテナオーケストレーションプラットフォームであるKubernetesの特定のバージョン番号。各バージョンには、新機能の追加、既存機能の改善、バグ修正、セキュリティパッチ、APIの変更（非推奨化や削除を含む）などが含まれます。
*   **リリースノート (Release Notes)**: ソフトウェア製品の新バージョンで追加・変更・修正された内容をまとめた文書。特に技術的な詳細や互換性に関する情報が含まれます。
*   **リリースブログ (Release Blog)**: ソフトウェア製品の新バージョンについて、主要な新機能やハイライトをより分かりやすい形で紹介するブログ記事。